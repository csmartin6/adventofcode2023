from dataclasses import dataclass
import bisect
from typing import List


@dataclass
class Mapping:
    source_start: int
    destination_start: int
    source_range: int

    @staticmethod
    def from_tuple(t):
        return Mapping(source_start=t[1], destination_start=t[0], source_range=t[2])

    def map(self, n):
        if self.source_start + self.source_range > n:
            return self.destination_start + (n - self.source_start)
        else:
            return n

    def map_span(self, span):

        span_start, span_end = span
        map_start = self.source_start
        map_end = self.source_start + self.source_range
        map_offset = self.destination_start - self.source_start
        # no overlap
        if map_start >= span_end or map_end < span_start:
            return None, [span]

        # span a subset of the map
        if map_start <= span_start and map_end >= span_end:
            return (span_start + map_offset, span_end + map_offset), []

        # map a subset of the span
        if map_start > span_start and map_end < span_end:
            return (map_start + map_offset, map_end + map_offset), [(span_start, map_start), (map_end, span_end)]

        # partial overlap on left
        if map_start <= span_start and map_end < span_end:
            return (span_start + map_offset, map_end + map_offset), [(map_end, span_end)]

        # partial overlap on right
        if map_start > span_start and map_end >= span_end:
            return (map_start + map_offset, span_end + map_offset), [(span_start, map_start)]

        print("something has gone wrong")


class RangeMap:
    mappings: List[Mapping]

    def __init__(self, tuples):
        self.mappings = sorted([Mapping.from_tuple(t) for t in tuples],
                               key=lambda m: m.source_start)

    @staticmethod
    def from_lines(lines, start, end):
        ts = []
        for i in range(start, end):
            ts.append([int(n) for n in lines[i].split()])
        return RangeMap(ts)

    def insert(self, t):
        self.mappings = bisect.insort(self.mappings, Mapping.from_tuple(t))

    def map(self, n):
        i = bisect.bisect(self.mappings, n, key=lambda m: m.source_start)
        if i == 0:
            return n
        mapping: Mapping = self.mappings[i - 1]
        if mapping.source_start + mapping.source_range > n:
            return mapping.destination_start + (n - mapping.source_start)
        else:
            return n

    def map_span(self, span):
        mapped_spans = []

        remaining_spans = [span]
        i = 0
        while len(remaining_spans) > 0 and i < len(self.mappings):
            mapping = self.mappings[i]
            new_remaining_spans = []
            for sp in remaining_spans:
                mapped_span, rs = mapping.map_span(sp)
                new_remaining_spans.extend(rs)
                if mapped_span is not None:
                    mapped_spans.append(mapped_span)

            remaining_spans = new_remaining_spans
            i += 1

        if len(remaining_spans) > 0:
            mapped_spans.extend(remaining_spans)

        return sorted(mapped_spans)


def parse_seed_line(line):
    return [int(n) for n in line.strip("seed: ").split()]


def run_maps(maps, seed):
    n = seed
    for m in maps:
        n = m.map(n)
    return n


if __name__ == '__main__':
    with open('data/day_05_input.txt') as f:
        lines = f.readlines()
    #
    # with open('data/day_05_example.txt') as f:
    #     lines = f.readlines()

    seeds = parse_seed_line(lines[0])

    seed_to_soil_index = next(i for i, l in enumerate(lines) if l.startswith("seed-to-soil map:"))
    soil_to_fertilizer_index = next(i for i, l in enumerate(lines) if l.startswith("soil-to-fertilizer map:"))
    fertilizer_to_water_index = next(i for i, l in enumerate(lines) if l.startswith("fertilizer-to-water map:"))
    water_to_light_index = next(i for i, l in enumerate(lines) if l.startswith("water-to-light map:"))
    light_to_temperature_index = next(i for i, l in enumerate(lines) if l.startswith("light-to-temperature map:"))
    temperature_to_humidity_index = next(i for i, l in enumerate(lines) if l.startswith("temperature-to-humidity map:"))
    humidity_to_location_index = next(i for i, l in enumerate(lines) if l.startswith("humidity-to-location map:"))

    seed_to_soil_map = RangeMap.from_lines(lines, seed_to_soil_index + 1, soil_to_fertilizer_index - 1)
    soil_to_fertilizer_map = RangeMap.from_lines(lines, soil_to_fertilizer_index + 1, fertilizer_to_water_index - 1)
    fertilizer_to_water_map = RangeMap.from_lines(lines, fertilizer_to_water_index + 1, water_to_light_index - 1)
    water_to_light_map = RangeMap.from_lines(lines, water_to_light_index + 1, light_to_temperature_index - 1)
    light_to_temperature_map = RangeMap.from_lines(lines, light_to_temperature_index + 1,
                                                   temperature_to_humidity_index - 1)
    temperature_to_humidity_map = RangeMap.from_lines(lines, temperature_to_humidity_index + 1,
                                                      humidity_to_location_index - 1)
    humidity_to_location_map = RangeMap.from_lines(lines, humidity_to_location_index + 1, len(lines))

    maps = [seed_to_soil_map,
            soil_to_fertilizer_map,
            fertilizer_to_water_map,
            water_to_light_map,
            light_to_temperature_map,
            temperature_to_humidity_map,
            humidity_to_location_map]

    locations = [run_maps(maps, s) for s in seeds]

    print(f"Part 1: Minimum Location: {min(locations)}")

    seeds = parse_seed_line(lines[0])
    orig_spans = [(seeds[2 * i], seeds[2 * i] + seeds[2 * i + 1]) for i in range(len(seeds) // 2)]

    min_locations = []
    for i, span in enumerate(orig_spans):

        # print(f"{i}: {span}")

        ogs = [span]
        for m in maps:
            new_ogs = []
            for og in ogs:
                new_ogs.extend(m.map_span(og))
            ogs = sorted(new_ogs)
        min_location = float('inf')
        for og in ogs:
            location = og[0]
            if location < min_location:
                min_location = location

        min_locations.append(min_location)
    print(f"Part 2: Minimum Location: {min(min_locations)}")

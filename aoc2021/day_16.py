from __future__ import annotations
from dataclasses import dataclass
from functools import reduce
from operator import mul


@dataclass(slots=True)
class Packet:
    version: int
    type_id: int


@dataclass(slots=True)
class Literal(Packet):
    value: int


@dataclass(slots=True)
class Operator(Packet):
    packets: list[Packet]


class Decoder:
    def __init__(self, bits: list[int]) -> None:
        self.offset = 0
        self.bits = bits

    def next_bit(self):
        self.offset += 1

    def read_number(self, length: int) -> int:
        number = 0
        for _ in range(length):
            number *= 2
            number += self.bits[self.offset]
            self.next_bit()
        return number

    def read_literal_value(self) -> int:
        number = 0

        while self.bits[self.offset] == 1:
            self.next_bit()
            number <<= 4
            number += self.read_number(4)

        self.next_bit()
        number <<= 4
        number += self.read_number(4)

        return number

    def read_packets_of_amount(self, amount: int) -> list[Packet]:
        return [self.decode_rec() for _ in range(amount)]

    def read_packets_of_length(self, length: int) -> list[Packet]:
        end_offset = self.offset + length
        subpackets = []
        while self.offset < end_offset:
            subpackets.append(self.decode_rec())
        return subpackets

    def decode_rec(self) -> Packet:
        version = self.read_number(3)
        type_id = self.read_number(3)

        if type_id == 4:
            return Literal(version, type_id, self.read_literal_value())

        length_type = self.bits[self.offset]
        self.next_bit()

        if length_type:
            number_of_subpackets = self.read_number(11)
            subpackets = self.read_packets_of_amount(number_of_subpackets)
        else:
            length_of_subpackets = self.read_number(15)
            subpackets = self.read_packets_of_length(length_of_subpackets)

        return Operator(version, type_id, subpackets)

    @classmethod
    def decode(cls, transmission: str) -> Packet:
        return cls.create(transmission).decode_rec()

    @classmethod
    def create(cls, transmission: str) -> Decoder:
        bits = []
        for char in transmission:
            bits += map(int, bin(int(char, base=16))[2:].zfill(4))
        return cls(bits)


def version_sum(packet: Packet) -> int:
    match packet:
        case Literal(version=version):
            return version
        case Operator(version=version, packets=packets):
            return version + sum(version_sum(p) for p in packets)
        case _:
            raise Exception("Unknown packet: ", packet)

def evaluate_operator(type_id: int, packets: list[Packet]) -> int:
    # pylint: disable=too-many-return-statements
    match type_id:
        case 0:
            return sum(evaluate(p) for p in packets)

        case 1:
            return reduce(mul, (evaluate(p) for p in packets), 1)

        case 2:
            return min(evaluate(p) for p in packets)

        case 3:
            return max(evaluate(p) for p in packets)

        case (5|6|7):
            first = evaluate(packets[0])
            second = evaluate(packets[1])

            if type_id == 5:
                return int(first > second)

            if type_id == 6:
                return int(first < second)

            return int(first == second)

        case _:
            raise Exception("Unknown type id: ", type_id)

def evaluate(packet: Packet) -> int:
    match packet:
        case Literal(value=value):
            return value

        case Operator(type_id=type_id, packets=packets):
            return evaluate_operator(type_id, packets)

        case _:
            raise Exception("Unknown packet: ", packet)


def first_task(transmission: str) -> int:
    packet = Decoder.decode(transmission)
    return version_sum(packet)


def second_task(transmission: str) -> int:
    packet = Decoder.decode(transmission)
    return evaluate(packet)

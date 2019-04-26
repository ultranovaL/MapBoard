from enum import Enum, unique


@unique
class OperationType(Enum):
    DrawType = 1
    MoveType = 2
    EditType = 3


@unique
class LineType(Enum):
    HighWay = 1
    BuildingHighWay = 2
    BuildingProvincialHighWay = 3
    XianRoad = 4
    PlaneRoad = 5
    MileageRoad = 6


@unique
class PointType(Enum):
    SanJiaoDian = 1
    TianWenDian = 2
    YanCong = 3
    ShuiTa = 4
    YouGuan = 5
    GuTa = 6
    FaDianChang = 7

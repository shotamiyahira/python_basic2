weather_information = [
        {'prefecture': '東京都', 'station': '渋谷', 'temperature': 6.5},
        {'prefecture': '東京都', 'station': '池袋', 'temperature': 7.0},
        {'prefecture': '東京都', 'station': '新橋', 'temperature': 7.5},

        {'prefecture': '大阪府', 'station': '梅田', 'temperature': 8.2},
        {'prefecture': '大阪府', 'station': '大阪', 'temperature': 9.3},
        {'prefecture': '大阪府', 'station': '堺', 'temperature': 9.5},

        {'prefecture': '福岡県', 'station': '博多', 'temperature': 13.0},
        {'prefecture': '福岡県', 'station': '太宰府', 'temperature': 15.0},
    ]

# 平均気温
temperature = [
    info ["temperature"] for info in weather_information
    ]
result = sum(temperature) / len(weather_information)
print(result)

# 大阪
station = [
    info["station"] for info in weather_information if info['prefecture'] == "大阪府"
    ]
print(",".join(station))

# 別解
# osaka_station = []
# for info in weather_information:
#     if info["prefecture"] == "大阪府":
#         osaka_station.append(info["station"])

# station_string = ",".join(osaka_station)
# print(station_string)

# 福岡の平均気温
temperature = [
    info ["temperature"] for info in weather_information if info['prefecture'] == "福岡県"
    ]
result = sum(temperature) / len(temperature)
print(result)

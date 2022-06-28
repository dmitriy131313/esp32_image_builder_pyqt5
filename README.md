# esp32_image_builder_pyqt5
Utility for creating a single binary firmware file for zero offset flashing with gui interface.

Applicable for ESP-IDF projects that are builded using Cmake.

1. It is necessary to create a custom partition table file with particular name - "partitions.csv". The script uses it to create a binary file.
2. Start script by main.py
3. Select folder with project
4. Make binary!

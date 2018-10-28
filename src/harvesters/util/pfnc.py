#!/usr/bin/env python3
# ----------------------------------------------------------------------------
#
# Copyright 2018 EMVA
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# ----------------------------------------------------------------------------


# Standard library imports

# Related third party imports

# Local application/library specific imports


# We create the following symbolics from the official PFNC table so the
# numeric values are all capitalized but this is an exception: We usually
# go with lower case in other Python files.
symbolics = {
    # As of 17-Feb-2017
    0x01080001: 'Mono8',
    0x01080002: 'Mono8s',
    0x01100003: 'Mono10',
    0x010C0004: 'Mono10Packed',
    0x01100005: 'Mono12',
    0x010C0006: 'Mono12Packed',
    0x01100007: 'Mono16',
    0x01080008: 'BayerGR8',
    0x01080009: 'BayerRG8',
    0x0108000A: 'BayerGB8',
    0x0108000B: 'BayerBG8',
    0x0110000C: 'BayerGR10',
    0x0110000D: 'BayerRG10',
    0x0110000E: 'BayerGB10',
    0x0110000F: 'BayerBG10',
    0x01100010: 'BayerGR12',
    0x01100011: 'BayerRG12',
    0x01100012: 'BayerGB12',
    0x01100013: 'BayerBG12',
    0x02180014: 'RGB8',
    0x02180015: 'BGR8',
    0x02200016: 'RGBa8',
    0x02200017: 'BGRa8',
    0x02300018: 'RGB10',
    0x02300019: 'BGR10',
    0x0230001A: 'RGB12',
    0x0230001B: 'BGR12',
    0x0220001C: 'RGB10V1Packed',
    0x0220001D: 'RGB10p32',
    0x020C001E: 'YUV411_8_UYYVYY',
    0x0210001F: 'YUV422_8_UYVY',
    0x02180020: 'YUV8_UYV',
    0x02180021: 'RGB8_Planar',
    0x02300022: 'RGB10_Planar',
    0x02300023: 'RGB12_Planar',
    0x02300024: 'RGB16_Planar',
    0x01100025: 'Mono14',
    0x010C0026: 'BayerGR10Packed',
    0x010C0027: 'BayerRG10Packed',
    0x010C0028: 'BayerGB10Packed',
    0x010C0029: 'BayerBG10Packed',
    0x010C002A: 'BayerGR12Packed',
    0x010C002B: 'BayerRG12Packed',
    0x010C002C: 'BayerGB12Packed',
    0x010C002D: 'BayerBG12Packed',
    0x0110002E: 'BayerGR16',
    0x0110002F: 'BayerRG16',
    0x01100030: 'BayerGB16',
    0x01100031: 'BayerBG16',
    0x02100032: 'YUV422_8',
    0x02300033: 'RGB16',
    0x02240034: 'RGB12V1Packed',
    0x02100035: 'RGB565p',
    0x02100036: 'BGR565p',
    0x01010037: 'Mono1p',
    0x01020038: 'Mono2p',
    0x01040039: 'Mono4p',
    0x0218003A: 'YCbCr8_CbYCr',
    0x0210003B: 'YCbCr422_8',
    0x020C003C: 'YCbCr411_8_CbYYCrYY',
    0x0218003D: 'YCbCr601_8_CbYCr',
    0x0210003E: 'YCbCr601_422_8',
    0x020C003F: 'YCbCr601_411_8_CbYYCrYY',
    0x02180040: 'YCbCr709_8_CbYCr',
    0x02100041: 'YCbCr709_422_8',
    0x020C0042: 'YCbCr709_411_8_CbYYCrYY',
    0x02100043: 'YCbCr422_8_CbYCrY',
    0x02100044: 'YCbCr601_422_8_CbYCrY',
    0x02100045: 'YCbCr709_422_8_CbYCrY',
    0x010A0046: 'Mono10p',
    0x010C0047: 'Mono12p',
    0x021E0048: 'BGR10p',
    0x02240049: 'BGR12p',
    0x0230004A: 'BGR14',
    0x0230004B: 'BGR16',
    0x0240004C: 'BGRa10',
    0x0228004D: 'BGRa10p',
    0x0240004E: 'BGRa12',
    0x0230004F: 'BGRa12p',
    0x02400050: 'BGRa14',
    0x02400051: 'BGRa16',
    0x010A0052: 'BayerBG10p',
    0x010C0053: 'BayerBG12p',
    0x010A0054: 'BayerGB10p',
    0x010C0055: 'BayerGB12p',
    0x010A0056: 'BayerGR10p',
    0x010C0057: 'BayerGR12p',
    0x010A0058: 'BayerRG10p',
    0x010C0059: 'BayerRG12p',
    0x020C005A: 'YCbCr411_8',
    0x0218005B: 'YCbCr8',
    0x021E005C: 'RGB10p',
    0x0224005D: 'RGB12p',
    0x0230005E: 'RGB14',
    0x0240005F: 'RGBa10',
    0x02280060: 'RGBa10p',
    0x02400061: 'RGBa12',
    0x02300062: 'RGBa12p',
    0x02400063: 'RGBa14',
    0x02400064: 'RGBa16',
    0x02200065: 'YCbCr422_10',
    0x02200066: 'YCbCr422_12',
    0x01080067: 'SCF1WBWG8',
    0x01100068: 'SCF1WBWG10',
    0x010A0069: 'SCF1WBWG10p',
    0x0110006A: 'SCF1WBWG12',
    0x010C006B: 'SCF1WBWG12p',
    0x0110006C: 'SCF1WBWG14',
    0x0110006D: 'SCF1WBWG16',
    0x0108006E: 'SCF1WGWB8',
    0x0110006F: 'SCF1WGWB10',
    0x010A0070: 'SCF1WGWB10p',
    0x01100071: 'SCF1WGWB12',
    0x010C0072: 'SCF1WGWB12p',
    0x01100073: 'SCF1WGWB14',
    0x01100074: 'SCF1WGWB16',
    0x01080075: 'SCF1WGWR8',
    0x01100076: 'SCF1WGWR10',
    0x010A0077: 'SCF1WGWR10p',
    0x01100078: 'SCF1WGWR12',
    0x010C0079: 'SCF1WGWR12p',
    0x0110007A: 'SCF1WGWR14',
    0x0110007B: 'SCF1WGWR16',
    0x0108007C: 'SCF1WRWG8',
    0x0110007D: 'SCF1WRWG10',
    0x010A007E: 'SCF1WRWG10p',
    0x0110007F: 'SCF1WRWG12',
    0x010C0080: 'SCF1WRWG12p',
    0x01100081: 'SCF1WRWG14',
    0x01100082: 'SCF1WRWG16',
    0x02300083: 'YCbCr10_CbYCr',
    0x021E0084: 'YCbCr10p_CbYCr',
    0x02300085: 'YCbCr12_CbYCr',
    0x02240086: 'YCbCr12p_CbYCr',
    0x02140087: 'YCbCr422_10p',
    0x02180088: 'YCbCr422_12p',
    0x02300089: 'YCbCr601_10_CbYCr',
    0x021E008A: 'YCbCr601_10p_CbYCr',
    0x0230008B: 'YCbCr601_12_CbYCr',
    0x0224008C: 'YCbCr601_12p_CbYCr',
    0x0220008D: 'YCbCr601_422_10',
    0x0214008E: 'YCbCr601_422_10p',
    0x0220008F: 'YCbCr601_422_12',
    0x02180090: 'YCbCr601_422_12p',
    0x02300091: 'YCbCr709_10_CbYCr',
    0x021E0092: 'YCbCr709_10p_CbYCr',
    0x02300093: 'YCbCr709_12_CbYCr',
    0x02240094: 'YCbCr709_12p_CbYCr',
    0x02200095: 'YCbCr709_422_10',
    0x02140096: 'YCbCr709_422_10p',
    0x02200097: 'YCbCr709_422_12',
    0x02180098: 'YCbCr709_422_12p',
    0x02200099: 'YCbCr422_10_CbYCrY',
    0x0214009A: 'YCbCr422_10p_CbYCrY',
    0x0220009B: 'YCbCr422_12_CbYCrY',
    0x0218009C: 'YCbCr422_12p_CbYCrY',
    0x0220009D: 'YCbCr601_422_10_CbYCrY',
    0x0214009E: 'YCbCr601_422_10p_CbYCrY',
    0x0220009F: 'YCbCr601_422_12_CbYCrY',
    0x021800A0: 'YCbCr601_422_12p_CbYCrY',
    0x022000A1: 'YCbCr709_422_10_CbYCrY',
    0x021400A2: 'YCbCr709_422_10p_CbYCrY',
    0x022000A3: 'YCbCr709_422_12_CbYCrY',
    0x021800A4: 'YCbCr709_422_12p_CbYCrY',
    0x021000A5: 'BiColorRGBG8',
    0x021000A6: 'BiColorBGRG8',
    0x022000A7: 'BiColorRGBG10',
    0x021400A8: 'BiColorRGBG10p',
    0x022000A9: 'BiColorBGRG10',
    0x021400AA: 'BiColorBGRG10p',
    0x022000AB: 'BiColorRGBG12',
    0x021800AC: 'BiColorRGBG12p',
    0x022000AD: 'BiColorBGRG12',
    0x021800AE: 'BiColorBGRG12p',
    0x010800AF: 'Coord3D_A8',
    0x010800B0: 'Coord3D_B8',
    0x010800B1: 'Coord3D_C8',
    0x021800B2: 'Coord3D_ABC8',
    0x021800B3: 'Coord3D_ABC8_Planar',
    0x021000B4: 'Coord3D_AC8',
    0x021000B5: 'Coord3D_AC8_Planar',
    0x011000B6: 'Coord3D_A16',
    0x011000B7: 'Coord3D_B16',
    0x011000B8: 'Coord3D_C16',
    0x023000B9: 'Coord3D_ABC16',
    0x023000BA: 'Coord3D_ABC16_Planar',
    0x022000BB: 'Coord3D_AC16',
    0x022000BC: 'Coord3D_AC16_Planar',
    0x012000BD: 'Coord3D_A32f',
    0x012000BE: 'Coord3D_B32f',
    0x012000BF: 'Coord3D_C32f',
    0x026000C0: 'Coord3D_ABC32f',
    0x026000C1: 'Coord3D_ABC32f_Planar',
    0x024000C2: 'Coord3D_AC32f',
    0x024000C3: 'Coord3D_AC32f_Planar',
    0x010800C4: 'Confidence1',
    0x010100C5: 'Confidence1p',
    0x010800C6: 'Confidence8',
    0x011000C7: 'Confidence16',
    0x012000C8: 'Confidence32f',
    0x010800C9: 'R8',
    0x010A00CA: 'R10',
    0x010C00CB: 'R12',
    0x011000CC: 'R16',
    0x010800CD: 'G8',
    0x010A00CE: 'G10',
    0x010C00CF: 'G12',
    0x011000D0: 'G16',
    0x010800D1: 'B8',
    0x010A00D2: 'B10',
    0x010C00D3: 'B12',
    0x011000D4: 'B16',
    0x010A00D5: 'Coord3D_A10p',
    0x010A00D6: 'Coord3D_B10p',
    0x010A00D7: 'Coord3D_C10p',
    0x010C00D8: 'Coord3D_A12p',
    0x010C00D9: 'Coord3D_B12p',
    0x010C00DA: 'Coord3D_C12p',
    0x021E00DB: 'Coord3D_ABC10p',
    0x021E00DC: 'Coord3D_ABC10p_Planar',
    0x022400DE: 'Coord3D_ABC12p',
    0x022400DF: 'Coord3D_ABC12p_Planar',
    0x021400F0: 'Coord3D_AC10p',
    0x021400F1: 'Coord3D_AC10p_Planar',
    0x021800F2: 'Coord3D_AC12p',
    0x021800F3: 'Coord3D_AC12p_Planar',
    0x021800F4: 'YCbCr2020_8_CbYCr',
    0x023000F5: 'YCbCr2020_10_CbYCr',
    0x021E00F6: 'YCbCr2020_10p_CbYCr',
    0x023000F7: 'YCbCr2020_12_CbYCr',
    0x022400F8: 'YCbCr2020_12p_CbYCr',
    0x020C00F9: 'YCbCr2020_411_8_CbYYCrYY',
    0x021000FA: 'YCbCr2020_422_8',
    0x021000FB: 'YCbCr2020_422_8_CbYCrY',
    0x022000FC: 'YCbCr2020_422_10',
    0x022000FD: 'YCbCr2020_422_10_CbYCrY',
    0x021400FE: 'YCbCr2020_422_10p',
    0x021400FF: 'YCbCr2020_422_10p_CbYCrY',
    0x02200100: 'YCbCr2020_422_12',
    0x02200101: 'YCbCr2020_422_12_CbYCrY',
    0x02180102: 'YCbCr2020_422_12p',
    0x02180103: 'YCbCr2020_422_12p_CbYCrY',
}

# 32-bit value layout
# |31            24|23            16|15            08|07            00|
# | C| Comp. Layout| Effective Size |            Pixel ID             |

# Custom flag
pfnc_custom = 0x80000000
# Component layout
pfnc_single_component = 0x01000000
pfnc_multiple_component = 0x02000000
pfnc_component_mask = 0x02000000
# Effective size
pfnc_pixel_size_mask = 0x00ff0000
pfnc_pixel_size_shift = 16


def get_effective_pixel_size(pixel_format_value):
    """
    Returns the effective pixel size (number of bits a pixel occupies in memory).
    This includes padding in many cases and the actually used bits are less.
    """
    return (pixel_format_value & pfnc_pixel_size_mask) >> \
           pfnc_pixel_size_shift


def is_custom(pixel_format_value):
    return (pixel_format_value & pfnc_custom) == pfnc_custom


def is_single_component(pixel_format_value):
    return (pixel_format_value & pfnc_component_mask) == pfnc_single_component


def is_multiple_component(pixel_format_value):
    return (pixel_format_value & pfnc_component_mask) == pfnc_multiple_component


def get_bits_per_pixel(data_format):
    """
    Returns the number of (used) bits per pixel.
    So without padding.
    Returns None if format is not known.
    """
    if data_format in component_8bit_formats:
        return 8
    elif data_format in component_10bit_formats:
        return 10
    elif data_format in component_12bit_formats:
        return 12
    elif data_format in component_14bit_formats:
        return 14
    elif data_format in component_16bit_formats:
        return 16
    # format not known
    return None


mono_location_formats = [
    'Raw', 'Mono', 'R', 'G', 'B',
    'Mono8', 'Mono10', 'Mono12', 'Mono14', 'Mono16',
    'Coord3D_A', 'Coord3D_B', 'Coord3D_C', 'Confidence',
]

lmn_444_location_formats = [
    'RGB', 'BGR',
    'YUV', 'YCbCr', 'YCbCr601', 'YCbCr709',
    'RGB8', 'RGB10', 'RGB12', 'RGB14', 'RGB16',
    'BGR8', 'BGR10', 'BGR12', 'BGR14', 'BGR16',
    'RGB8Packed',
    'Coord3D_ABC',
]

lmn_422_location_formats = [
    'YUV422', 'YCbCr422', 'YCbCr601_422', 'YCbCr709_422',
]

lmn_411_location_formats = [
    'YUV411', 'YCbCr411', 'YCbCr601_411', 'YCbCr709_411',
]

lmno_4444_location_formats = [
    'aRGB', 'YRGB', 'RGBa', 'BGRa',
    'RGBa8', 'RGBa10', 'RGBa12', 'RGBa14', 'RGBa16',
    'BGRa8', 'BGRa10', 'BGRa12', 'BGRa14', 'BGRa16',
]

lm_44_location_formats = [
    'Coord3D_AC',
]

bayer_location_formats = [
    #
    'BayerGR8', 'BayerGB8', 'BayerRG8', 'BayerBG8',
    #
    'BayerGR12', 'BayerGB12', 'BayerRG12', 'BayerBG12',
    #
    'BayerGR10', 'BayerGB10', 'BayerRG10', 'BayerBG10',
    #
    'BayerGR16', 'BayerRG16', 'BayerGB16', 'BayerBG16',
    #
    'BayerGR32', 'BayerRG32', 'BayerGB32', 'BayerBG32',
]

uint8_formats = [
    #
    'Mono8',
    #
    'RGB8', 'RGB8Packed', 'RGBa8',
    #
    'BGR8', 'BGRa8',
    #
    'BayerGR8', 'BayerGB8', 'BayerRG8', 'BayerBG8',
    #
    'Confidence8'
]

uint16_formats = [
    #
    'Mono10', 'Mono12', 'Mono14', 'Mono16',
    #
    'RGB10', 'RGB12', 'RGB14', 'RGB16',
    #
    'BGR10', 'BGR12', 'BGR14', 'BGR16',
    #
    'RGBa10', 'RGBa12', 'RGBa14', 'RGBa16',
    #
    'BGRa10', 'BGRa12', 'BGRa14', 'BGRa16',
    #
    'BayerGR10', 'BayerGB10', 'BayerRG10', 'BayerBG10',
    #
    'BayerGR12', 'BayerGB12', 'BayerRG12', 'BayerBG12',
    #
    'BayerGR16', 'BayerRG16', 'BayerGB16', 'BayerBG16',
    #
    'Coord3D_C16'
]

uint32_formats = [
    'Mono32',
]

float32_formats = [
    'Coord3D_A32f', 'Coord3D_B32f', 'Coord3D_C32f',
]

component_8bit_formats = [
    #
    'Mono8',
    #
    'RGB8', 'RGBa8',
    #
    'BGR8', 'BGRa8',
    #
    'BayerGR8', 'BayerGB8', 'BayerRG8', 'BayerBG8',
    #
    'Confidence8'
]

component_10bit_formats = [
    #
    'Mono10',
    #
    'RGB10', 'RGBa10',
    #
    'BGR10', 'BGRa10',
    #
    'BayerGR10', 'BayerGB10', 'BayerRG10', 'BayerBG10',
]

component_12bit_formats = [
    #
    'Mono12',
    #
    'RGB12', 'RGBa12',
    #
    'BGR12', 'BGRa12',
    #
    'BayerGR12', 'BayerGB12', 'BayerRG12', 'BayerBG12',
]

component_14bit_formats = [
    #
    'Mono14',
    #
    'RGB14', 'RGBa14',
    #
    'BGR14', 'BGRa14',
]

component_16bit_formats = [
    #
    'Mono16',
    #
    'RGB16', 'RGBa16',
    #
    'BayerGR16', 'BayerRG16', 'BayerGB16', 'BayerBG16',
    #
    'Coord3D_C16',
]

component_2d_formats = [
    #
    'Mono8', 'Mono10', 'Mono12', 'Mono14', 'Mono16',
    #
    'RGB8', 'RGB10', 'RGB12', 'RGB14', 'RGB16',
    #
    'BGR8', 'BGR10', 'BGR12', 'BGR14', 'BGR16',
    #
    'RGBa8', 'RGBa10', 'RGBa12', 'RGBa14', 'RGBa16',
    #
    'BGRa8', 'BGRa10', 'BGRa12', 'BGRa14', 'BGRa16',
    #
    'BayerGR8', 'BayerGB8', 'BayerRG8', 'BayerBG8',
    #
    'BayerGR10', 'BayerGB10', 'BayerRG10', 'BayerBG10',
    #
    'BayerGR12', 'BayerGB12', 'BayerRG12', 'BayerBG12',
    #
    'BayerGR16', 'BayerRG16', 'BayerGB16', 'BayerBG16',
    #
    'Coord3D_A32f', 'Coord3D_B32f', 'Coord3D_C32f',
    'Coord3D_C16',
    #
    'Confidence1', 'Confidence1p', 'Confidence8', 'Confidence16',
    'Confidence32f',
]

rgb_formats = [
    #
    'RGB8', 'RGB10', 'RGB12', 'RGB14', 'RGB16',
]

rgba_formats = [
    #
    'RGBa8', 'RGBa10', 'RGBa12', 'RGBa14', 'RGBa16',
]

bgr_formats = [
    #
    'BGR8', 'BGR10', 'BGR12', 'BGR14', 'BGR16',
]

bgra_formats = [
    #
    'BGRa8', 'BGRa10', 'BGRa12', 'BGRa14', 'BGRa16',
]

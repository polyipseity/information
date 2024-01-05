/**
 * @file DR16.hpp
 * @author JIANG Yicheng (EthenJ@outlook.sg)
 * @brief
 * @version 0.1
 * @date 2023-10-18
 *
 * @copyright This file is only for HKUST Enterprize RM2024 internal
 * competition. All Rights Reserved.
 */

#include "AppConfig.h"
#if USE_DR16

#ifndef DR16_UART
#define DR16_UART huart1
#endif

#include "main.h"
#include "usart.h"

namespace DR16
{

/* ----------------------- RC Channel Properties---------------------------- */
constexpr uint16_t CH_VALUE_MIN = 364;   // the minimum value of a channel
constexpr uint16_t CH_VALUE_MID = 1024;  // the middle value of a channel
constexpr uint16_t CH_VALUE_MAX = 1684;  // the maximum value of a channel
constexpr uint16_t CH_VALUE_ABS_RANGE =
    ((CH_VALUE_MAX - CH_VALUE_MIN) / 2);  // the absolute range of a channel

/* ----------------------- RC Switch Definition----------------------------- */
constexpr uint16_t SW_UP   = 1;  // switch up
constexpr uint16_t SW_MID  = 3;  // switch middle
constexpr uint16_t SW_DOWN = 2;  // switch down
/*------------------------ PC Key Definition-------------------------------- */
constexpr uint16_t KEY_W     = 0x01 << 0;
constexpr uint16_t KEY_S     = 0x01 << 1;
constexpr uint16_t KEY_A     = 0x01 << 2;
constexpr uint16_t KEY_D     = 0x01 << 3;
constexpr uint16_t KEY_Q     = 0x01 << 6;
constexpr uint16_t KEY_E     = 0x01 << 7;
constexpr uint16_t KEY_R     = 0x01 << 8;
constexpr uint16_t KEY_F     = 0x01 << 9;
constexpr uint16_t KEY_G     = 0x01 << 10;
constexpr uint16_t KEY_Z     = 0x01 << 11;
constexpr uint16_t KEY_X     = 0x01 << 12;
constexpr uint16_t KEY_C     = 0x01 << 13;
constexpr uint16_t KEY_V     = 0x01 << 14;
constexpr uint16_t KEY_B     = 0x01 << 15;
constexpr uint16_t KEY_SHIFT = 0x01 << 4;
constexpr uint16_t KEY_CTRL  = 0x01 << 5;

/**
 * @brief RC data structure
 */
struct RcData
{
    /**
     * @brief remote controller channel data
     */
    struct
    {
        uint16_t ch0 = 1024U;
        uint16_t ch1 = 1024U;
        uint16_t ch2 = 1024U;
        uint16_t ch3 = 1024U;
        uint8_t s1   = 0U;
        uint8_t s2   = 0U;
        uint16_t ch4 = 1024U;
    } rc;

    /**
     * @brief mouse data
     */
    struct
    {
        int16_t x   = 0;
        int16_t y   = 0;
        int16_t z   = 0;
        bool pressL = 0;
        bool pressR = 0;
    } mouse;

    /**
     * @brief keyboard data
     */
    uint16_t key = 0U;

    /**
     * @brief connection status
     */
    bool isConnected = false;
};

/**
 * @brief Get the DR16 data
 *
 * @return const volatile RcData &
 */
const volatile RcData &getRcData();

/**
 * @brief Check if the DR16 is connected
 *
 * @return true
 * @return false
 */
bool isConnected();

/**
 * @brief initialize the DR16, call this function before using the DR16
 */
void init(UART_HandleTypeDef *huart = &DR16_UART);

float inline normalizeChannel(uint16_t channel)
{
    if (channel < CH_VALUE_MIN or channel > CH_VALUE_MAX)
    {
        channel = CH_VALUE_MID;
    }

    float percent =
        static_cast<float>(channel - CH_VALUE_MID) / CH_VALUE_ABS_RANGE;
    if (percent < 0.01f and percent > -0.01f)
    {
        percent = 0.0f;
    }
    return percent;
}

}  // namespace DR16
#endif  // DR16_UART
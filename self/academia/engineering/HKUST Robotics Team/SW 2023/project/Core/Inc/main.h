/* USER CODE BEGIN Header */
/**
 ******************************************************************************
 * @file           : main.h
 * @brief          : Header for main.c file.
 *                   This file contains the common defines of the application.
 ******************************************************************************
 * @attention
 *
 * Copyright (c) 2023 STMicroelectronics.
 * All rights reserved.
 *
 * This software is licensed under terms that can be found in the LICENSE file
 * in the root directory of this software component.
 * If no LICENSE file comes with this software, it is provided AS-IS.
 *
 ******************************************************************************
 */
/* USER CODE END Header */

/* Define to prevent recursive inclusion -------------------------------------*/
#ifndef __MAIN_H
#define __MAIN_H

#ifdef __cplusplus
extern "C" {
#endif

/* Includes ------------------------------------------------------------------*/
#include "stm32f4xx_hal.h"

/* Private includes ----------------------------------------------------------*/
/* USER CODE BEGIN Includes */

/* USER CODE END Includes */

/* Exported types ------------------------------------------------------------*/
/* USER CODE BEGIN ET */

/* USER CODE END ET */

/* Exported constants --------------------------------------------------------*/
/* USER CODE BEGIN EC */

/* USER CODE END EC */

/* Exported macro ------------------------------------------------------------*/
/* USER CODE BEGIN EM */

/* USER CODE END EM */

/* Exported functions prototypes ---------------------------------------------*/
void Error_Handler(void);

/* USER CODE BEGIN EFP */

/* USER CODE END EFP */

/* Private defines -----------------------------------------------------------*/
#define CAM_D7_Pin GPIO_PIN_13
#define CAM_D7_GPIO_Port GPIOC
#define PWM1_Pin GPIO_PIN_0
#define PWM1_GPIO_Port GPIOA
#define CAM_HREF_Pin GPIO_PIN_1
#define CAM_HREF_GPIO_Port GPIOA
#define CAM_WRST_Pin GPIO_PIN_4
#define CAM_WRST_GPIO_Port GPIOA
#define TFT_SCK_Pin GPIO_PIN_5
#define TFT_SCK_GPIO_Port GPIOA
#define TFT_RES_Pin GPIO_PIN_6
#define TFT_RES_GPIO_Port GPIOA
#define TFT_MOSI_Pin GPIO_PIN_7
#define TFT_MOSI_GPIO_Port GPIOA
#define TFT_DC_Pin GPIO_PIN_4
#define TFT_DC_GPIO_Port GPIOC
#define TFT_CS_Pin GPIO_PIN_5
#define TFT_CS_GPIO_Port GPIOC
#define TFT_BL_Pin GPIO_PIN_0
#define TFT_BL_GPIO_Port GPIOB
#define CAM_WEN_Pin GPIO_PIN_1
#define CAM_WEN_GPIO_Port GPIOB
#define Boot1_Pin GPIO_PIN_2
#define Boot1_GPIO_Port GPIOB
#define CAM_SCL_Pin GPIO_PIN_10
#define CAM_SCL_GPIO_Port GPIOB
#define CAM_SDA_Pin GPIO_PIN_11
#define CAM_SDA_GPIO_Port GPIOB
#define CAM_VSYNC_Pin GPIO_PIN_14
#define CAM_VSYNC_GPIO_Port GPIOB
#define CAM_VSYNC_EXTI_IRQn EXTI15_10_IRQn
#define CAM_RCLK_Pin GPIO_PIN_15
#define CAM_RCLK_GPIO_Port GPIOB
#define CAM_D0_Pin GPIO_PIN_6
#define CAM_D0_GPIO_Port GPIOC
#define CAM_D1_Pin GPIO_PIN_7
#define CAM_D1_GPIO_Port GPIOC
#define CAM_D2_Pin GPIO_PIN_8
#define CAM_D2_GPIO_Port GPIOC
#define CAM_D3_Pin GPIO_PIN_9
#define CAM_D3_GPIO_Port GPIOC
#define CAM_RRST_Pin GPIO_PIN_8
#define CAM_RRST_GPIO_Port GPIOA
#define CAM_OE_Pin GPIO_PIN_15
#define CAM_OE_GPIO_Port GPIOA
#define CAM_D4_Pin GPIO_PIN_10
#define CAM_D4_GPIO_Port GPIOC
#define CAM_D5_Pin GPIO_PIN_11
#define CAM_D5_GPIO_Port GPIOC
#define CAM_D6_Pin GPIO_PIN_12
#define CAM_D6_GPIO_Port GPIOC
#define BTN2_Pin GPIO_PIN_2
#define BTN2_GPIO_Port GPIOD
#define BTN1_Pin GPIO_PIN_3
#define BTN1_GPIO_Port GPIOB
#define LED4_Pin GPIO_PIN_4
#define LED4_GPIO_Port GPIOB
#define LED3_Pin GPIO_PIN_5
#define LED3_GPIO_Port GPIOB
#define LED2_Pin GPIO_PIN_6
#define LED2_GPIO_Port GPIOB
#define LED1_Pin GPIO_PIN_7
#define LED1_GPIO_Port GPIOB
/* USER CODE BEGIN Private defines */

#define gpio_set(gpio) HAL_GPIO_WritePin(gpio##_GPIO_Port, gpio##_Pin, GPIO_PIN_SET)
#define gpio_reset(gpio) HAL_GPIO_WritePin(gpio##_GPIO_Port, gpio##_Pin, GPIO_PIN_RESET)
#define gpio_toggle(gpio) HAL_GPIO_TogglePin(gpio##_GPIO_Port, gpio##_Pin)
#define gpio_read(gpio) HAL_GPIO_ReadPin(gpio##_GPIO_Port, gpio##_Pin)

#define led_on(led) gpio_reset(led) // notice that reset the pin turns the led on
#define led_off(led) gpio_set(led)
#define led_toggle(led) gpio_toggle(led)
#define btn_read(btn) gpio_read(btn)

#define __forceinline __attribute__((__always_inline__)) inline

/* USER CODE END Private defines */

#ifdef __cplusplus
}
#endif

#endif /* __MAIN_H */

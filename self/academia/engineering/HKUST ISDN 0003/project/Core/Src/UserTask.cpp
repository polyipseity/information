/**
 * @file UserTask.cpp
 * @author JIANG Yicheng  RM2024 (EthenJ@outlook.sg)
 * @author GUO, Zilin
 * @brief Lecture 7 PID tutorial template codes
 * @version
 * @date 2022-08-20
 *
 * @copyright Copyright (c) 2024
 */
#include "AppConfig.h"
#include "FreeRTOS.h"
#include "PID.hpp"
#include "main.h"
#include "task.h"

/*  In this tutorial, we provide our motor driver for you.
    But you need to implement it individually in our RDC. */
#include "DJIMotor.hpp"

/*Allocate the stack for our PID task*/
StackType_t uxPIDTaskStack[configMINIMAL_STACK_SIZE];
/*Declare the PCB for our PID task*/
StaticTask_t xPIDTaskTCB;

#define TUTOTIAL7_MOTOR_DEFAULT_ID \
    0x205UL  // The default motor ID in this tutorial

float targetMotorPos = 0.0f;  // The target position of the motor

/**
 * @brief Our motor PID Controlling task on the FreeRTOS
 * @brief In this task, we get the output from our pre-defined PID module, and
 * set it to the motor module, then transmit it
 * @brief The "DJIMotor" "PID" is wrapped by namespace or a class, which
 * achieves the "modulization" we have discussed in Lecture 1
 */

void PIDTask(void *)
{
    /**
     * @example
     * @remark We construct a PID instance from the PID class here.
     */
    DJIMotor::DJIMotor &motor = DJIMotor::getMotor(
        TUTOTIAL7_MOTOR_DEFAULT_ID);  // Get the motor instance with ID 0X205
    motor.setCurrentLimit(30000);     // Set the motor's output limit.

    /* Your user layer codes begin here*/
    /*=================================================*/
    // Control::PID motorPID(100, 0, 0); // Declare a PID instance with Kp = 100

    /* Your user layer codes end here*/
    /*=================================================*/
    while (true)
    {
        /* Your user layer codes in loop begin here*/
        /*=================================================*/

        /* Your user layer codes in loop end here*/
        /*=================================================*/
        DJIMotor::sendMotorGroup(1);  // Transmit the data to the motor, which
                                      // has already been implemented by you

        vTaskDelay(1);  // Delay and block the task for 1ms.
        // Note, from now on, when using "FreeRTOS", we use "vTaskDelay(tick)"
        // instead of HAL_Delay(tick)
    }
}

/*Allocate the stack for our target update task*/
StackType_t uxTargetUpdateTaskStack[configMINIMAL_STACK_SIZE];
/*Declare the PCB for our target update task*/
StaticTask_t xTargetUpdateTaskTCB;

/**
 * @brief Our target update task on the FreeRTOS
 * @brief In this task, we update the target position of the motor
 */

void targetUpdateTask(void *)
{
    GPIO_PinState lastButtonState = GPIO_PIN_RESET;
    GPIO_PinState buttonState     = GPIO_PIN_RESET;
    uint8_t state                 = 0;
    while (true)
    {
        buttonState = HAL_GPIO_ReadPin(SW_GPIO_Port, SW_Pin);

        if (buttonState == GPIO_PIN_SET && lastButtonState == GPIO_PIN_RESET)
        {
            state += 1;
            state %= 2;
        }

        if (state == 0)
        {
            targetMotorPos = 0.0f;
        }
        else
        {
            targetMotorPos = 1.0f;
        }

        vTaskDelay(1);  // Delay and block the task for 1000ms.
    }
}

/**
 * @brief Intialize the module and create the user task
 * @note  In this tutorial, you do not need to care about these parts
 */

void startUserTasks()
{
    DJIMotor::init();  // Initalize the DJIMotor
    xTaskCreateStatic(PIDTask,
                      "pid task",
                      configMINIMAL_STACK_SIZE,
                      NULL,
                      1,
                      uxPIDTaskStack,
                      &xPIDTaskTCB);  // Add our PID task into the scheduler
    xTaskCreateStatic(targetUpdateTask,
                      "target update task",
                      configMINIMAL_STACK_SIZE,
                      NULL,
                      1,
                      uxTargetUpdateTaskStack,
                      &xTargetUpdateTaskTCB);  // Add our target update task
                                               // into the scheduler
}

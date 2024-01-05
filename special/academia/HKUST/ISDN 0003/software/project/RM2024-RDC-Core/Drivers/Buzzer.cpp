#include "Buzzer.hpp"

#if USE_BUZZER

#include "FreeRTOS.h"
#include "queue.h"
#include "task.h"
#include "tim.h"

namespace Buzzer
{

static inline uint16_t hz2psc(float freq) { return (uint16_t)((float)BUZZER_TIM_CLOCK / (BUZZER_TIM.Init.Period + 1) / freq); }
static inline uint16_t intensityFloatToUInt(float intensity) { return (BUZZER_TIM.Init.Period + 1) * intensity; }

static void buzzerOn(const uint16_t &psc, const uint16_t &comp)
{
    __HAL_TIM_SET_PRESCALER(&BUZZER_TIM, psc);
    __HAL_TIM_SET_COMPARE(&BUZZER_TIM, BUZZER_TIM_CHANNEL, comp);
}
static void buzzerOff(void) { __HAL_TIM_SetCompare(&BUZZER_TIM, BUZZER_TIM_CHANNEL, 0); }

static StaticQueue_t xNoteQueue;
static uint8_t ucNoteQueueStorageArea[sizeof(Note) * BUZZER_QUEUE_LENGTH];
static QueueHandle_t xNoteQueueHandle;

void playNote(const Note &note)
{
    // BaseType_t xHigherPriorityTaskWoken = pdFALSE;
    // xQueueSendToBackFromISR(xNoteQueueHandle, &note, &xHigherPriorityTaskWoken);
    xQueueSendToBack(xNoteQueueHandle, &note, 1);
    // portYIELD_FROM_ISR(xHigherPriorityTaskWoken);
}

static StackType_t uxBuzzerTaskStack[configMINIMAL_STACK_SIZE];
static StaticTask_t xBuzzerTaskTCB;

static void buzzerTask(void *pvPara)
{
    HAL_TIM_PWM_Start(&BUZZER_TIM, BUZZER_TIM_CHANNEL);

    while (true)
    {
        static Note note;
        if (xQueueReceive(xNoteQueueHandle, &note, portMAX_DELAY) == pdTRUE)
        {
            buzzerOn(hz2psc(note.freq), intensityFloatToUInt(note.intensity));
            vTaskDelay(note.onDuration);
            buzzerOff();
            vTaskDelay(note.offDuration);
        }
    }
}
void init()
{
    xNoteQueueHandle = xQueueCreateStatic(BUZZER_QUEUE_LENGTH, sizeof(Note), ucNoteQueueStorageArea, &xNoteQueue);
    xTaskCreateStatic(buzzerTask, "buzzer", configMINIMAL_STACK_SIZE, NULL, 0, uxBuzzerTaskStack, &xBuzzerTaskTCB);
}

}  // namespace Buzzer
#endif
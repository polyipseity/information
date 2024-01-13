#pragma once

#include "AppConfig.h"

#if USE_BUZZER
#include "main.h"
namespace Buzzer
{

void init();

struct Note
{
    float freq;
    uint32_t onDuration;
    uint32_t offDuration;
    float intensity;
};

/**
 * @brief Play a note
 * @param note
 */
void playNote(const Note &note);

}  // namespace Buzzer

#endif
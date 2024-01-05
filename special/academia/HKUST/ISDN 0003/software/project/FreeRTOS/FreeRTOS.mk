#######################################
# RM2023 FreeRTOS makefile
# 
# @author: JIANG Yicheng (RM2023)
#
# This makefile is only for HKUST Enterprize RM2023 internal competition.
#######################################

# Sources
FreeRTOS_SRC =  \
$(FreeRTOS_PATH)/sources/croutine.c \
$(FreeRTOS_PATH)/sources/event_groups.c \
$(FreeRTOS_PATH)/sources/list.c \
$(FreeRTOS_PATH)/sources/queue.c \
$(FreeRTOS_PATH)/sources/stream_buffer.c \
$(FreeRTOS_PATH)/sources/tasks.c \
$(FreeRTOS_PATH)/sources/timers.c

FreeRTOS_SRC +=  \
$(FreeRTOS_PATH)/portable/GCC/ARM_CM3/port.c 

# Includes
FreeRTOS_INC = -I$(FreeRTOS_PATH)/include

FreeRTOS_INC += -I$(FreeRTOS_PATH)/portable/GCC/ARM_CM3/


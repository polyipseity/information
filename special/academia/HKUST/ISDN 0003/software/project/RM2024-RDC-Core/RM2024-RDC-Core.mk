#######################################
# Sources
#######################################
# C Sources
C_SRC = 

# C++ Sources
CPP_SRC =  


CPP_SRC += \
$(wildcard $(CORE_DIR)/Control/*.cpp) \
$(wildcard $(CORE_DIR)/Drivers/*.cpp) \
$(wildcard $(CORE_DIR)/Communication/*.cpp) \
$(wildcard $(CORE_DIR)/Utils/*.cpp)

O_SRC += \
$(wildcard $(CORE_DIR)/Drivers/*.o) 


# ASM Sources
AS_SRC = 


#######################################
# Defines
#######################################
# ASM Defines
AS_DEF =

# Defines
DEFS = \
-DTRUE=1 \
-DFALSE=0

#######################################
# Includes
#######################################
# ASM Includes
AS_INC =

# Includes
INC =  \
-I$(CORE_DIR)/Control \
-I$(CORE_DIR)/Drivers  

#######################################
# Add to makefile
#######################################
C_SOURCES += $(C_SRC) 

CPP_SOURCES += $(CPP_SRC)

ASM_SOURCES += $(AS_SRC)

AS_DEFS += $(AS_DEF)

C_DEFS += $(DEFS) -DAPP_NAME=$(TARGET)

AS_INCLUDES += $(AS_INC)

C_INCLUDES += $(INC) 

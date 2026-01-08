################################################################################
# Automatically-generated file. Do not edit!
################################################################################

# Add inputs and outputs from these tool invocations to the build variables 
C_SRCS += \
../Core/Lib/TestInterrupt/TestInterruptGPIO/GPIOInterrupt.c 

OBJS += \
./Core/Lib/TestInterrupt/TestInterruptGPIO/GPIOInterrupt.o 

C_DEPS += \
./Core/Lib/TestInterrupt/TestInterruptGPIO/GPIOInterrupt.d 


# Each subdirectory must supply rules for building sources it contributes
Core/Lib/TestInterrupt/TestInterruptGPIO/GPIOInterrupt.o: ../Core/Lib/TestInterrupt/TestInterruptGPIO/GPIOInterrupt.c
	arm-none-eabi-gcc "$<" -mcpu=cortex-m4 -std=gnu11 -g3 -DUSE_HAL_DRIVER -DSTM32F401xE -DDEBUG -c -I../Drivers/CMSIS/Include -I../Drivers/STM32F4xx_HAL_Driver/Inc -I../Core/Inc -I../Drivers/CMSIS/Device/ST/STM32F4xx/Include -I../Drivers/STM32F4xx_HAL_Driver/Inc/Legacy -O0 -ffunction-sections -fdata-sections -Wall -fstack-usage -MMD -MP -MF"Core/Lib/TestInterrupt/TestInterruptGPIO/GPIOInterrupt.d" -MT"$@" --specs=nano.specs -mfpu=fpv4-sp-d16 -mfloat-abi=hard -mthumb -o "$@"


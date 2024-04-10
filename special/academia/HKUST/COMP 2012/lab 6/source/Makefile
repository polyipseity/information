# Define the compiler
CXX=g++

# Define compiler options, -Wall generates all warning messages
CXXFLAGS=-Wall -std=c++11

# Define the name of the executable file
TARGET=lab6.exe

# Define header files dependencies
HEADERS=matrix.h

# Default target
all: $(TARGET)

# Rule: How to generate the executable file from main.cpp and matrix.h
$(TARGET): main.cpp $(HEADERS)
	$(CXX) $(CXXFLAGS) main.cpp -o $(TARGET)

# Clean up compiled files
clean:
	rm -f $(TARGET)

# Declare phony targets
.PHONY: all clean

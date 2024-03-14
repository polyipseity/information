# This Makefile is designed to compile an executable
# from multiple C++ source files.

# Change the following 2 variables as necessary
ASGN_NAME = lab4.exe	# Name of assignment
SRCS = ProductCollection.cpp OrdinaryOrder.cpp MemberOrder.cpp main.cpp	# .cpp files required to compile

# Definition of variables
CPPFLAGS = -std=c++11 -Wall
OBJS = $(SRCS:.cpp=.o)
DEPS = $(SRCS:.cpp=.d)
EXE = $(ASGN_NAME).exe

# Rules: 
# target: dependencies
#   command used to create the target
$(EXE): $(OBJS) 
	g++ $(CPPFLAGS) -o $@ $(OBJS)

# To include the .d dependency files
-include $(DEPS)

# -MMD -MP creates the .d dependency files
.cpp.o:; g++ $(CPPFLAGS) -MMD -MP -c $<

clean:;	rm $(EXE) $(OBJS) $(DEPS)
ASGN_NAME = pa1
SRCS = main.cpp Menu.cpp Order.cpp OrderList.cpp Buyer.cpp Food.cpp

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

# Windows: change 'rm' to 'del'
clean:;	rm $(EXE) $(OBJS) $(DEPS)
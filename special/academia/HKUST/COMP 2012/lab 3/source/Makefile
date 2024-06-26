CC=gcc
CXX=g++
RM=rm -f
CPPFLAGS=-Wall -Wpedantic -fsanitize=address,leak,undefined -std=c++11

SRCS=$(wildcard *.cpp)
OBJS=$(subst .cpp,.o,$(SRCS))
DEPS=$(subst .cpp,.d,$(SRCS))
EXE=lab3

all: $(EXE)

clean:
	$(RM) $(OBJS) $(DEPS)

distclean: clean
	$(RM) $(EXE)

$(EXE): $(OBJS)
	$(CXX) $(CPPFLAGS) -o $@ $^

.cpp.o:
	$(CXX) $(CPPFLAGS) -MMD -MP -c $<

-include $(DEPS)

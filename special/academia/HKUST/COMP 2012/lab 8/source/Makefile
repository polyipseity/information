CXX = g++
CXXFLAGS = -Wall -g -std=c++11


main: main.o ShoppingCart.o
	$(CXX) $(CXXFLAGS) -o lab8.exe main.o ShoppingCart.o

main.o: main.cpp ShoppingCart.h
	$(CXX) $(CXXFLAGS) -c main.cpp

ShoppingCart.o: ShoppingCart.cpp ShoppingCart.h
	$(CXX) $(CXXFLAGS) -c ShoppingCart.cpp

clean:
	rm -f *.o main

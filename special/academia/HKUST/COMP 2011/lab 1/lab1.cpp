#include <iostream>

int main()
{
	int width{}, height{};

	std::cout << "Please input the width of the rectangle: ";
	std::cin >> width;
	std::cout << "Please input the height of the rectangle: ";
	std::cin >> height;

	if (width <= 0 || height <= 0)
	{
		std::cout << "Error: the width and height must be positive!";
	}
	else
	{
		std::cout << "The perimeter of the rectangle is " << (width + height) * 2;
	}
	std::cout << std::endl;

	return 0;
}

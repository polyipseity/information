// === Region: Project Declaration ===
//
//  COMP2011 Fall 2023
//  PA1: A Simpified Robot Wars Game
//
//  Your name:
//  Your ITSC email:           @connect.ust.hk
//
//  Declaration:
//  I declare that I am not involved in plagiarism
//  I understand that both parties (i.e., students providing the codes and students copying the codes) will receive 0 marks.
//
//  Project TA: CHUNG, Peter (cspeter@cse.ust.hk)
//
//  For code-level questions, please send a direct email to the above TA.
//  Asking questions with code blocks in a public discussion forum (e.g., Piazza) may cause plagiarism issues
//  Usually, you will get the quickest response via a direct email.
//
// =====================================

// === Region: Headers ===
// iostream and cstring are included.
// Do not include extra header files
// =======================
#include <iostream>
#include <cstring>
using namespace std;

// === Region: Constants ===
// Useful constants are defined for this project assignment
// =======================
const int MAX_ROWS = 20;
const int MAX_COLS = 30;
const int MAX_ACTION_TEXT_LENGTH = 10 + 1;    // array size for the action text, +1 for the NULL character
const int MAX_DIRECTION_TEXT_LENGTH = 10 + 1; // array size for the direction text, +1 for the NULL character
const int MAX_NUM_ROBOTS = 26;                // Note: Robots are named from A..Z
const char CHAR_EMPTY = '.';
const char CHAR_END_INPUT = '!';

const char DIRECTION_EAST = 'e';
const char DIRECTION_WEST = 'w';
const char DIRECTION_SOUTH = 's';
const char DIRECTION_NORTH = 'n';
const char DIRECTION_ERROR = '!';

const char DIRECTION_EAST_TEXT[] = "east";
const char DIRECTION_WEST_TEXT[] = "west";
const char DIRECTION_SOUTH_TEXT[] = "south";
const char DIRECTION_NORTH_TEXT[] = "north";
const char DIRECTION_ERROR_TEXT[] = "error";

const char ACTION_MOVE = 'm';
const char ACTION_HIT = 'h';
const char ACTION_SHOOT = 's';
const char ACTION_ERROR = '!';

const char ACTION_MOVE_TEXT[] = "moves";
const char ACTION_HIT_TEXT[] = "hits";
const char ACTION_SHOOT_TEXT[] = "shoots";

const int STATUS_ACTION_MOVE_NOT_IMPLMENTED = 0;
const int STATUS_ACTION_MOVE_SUCCESS = 1;
const int STATUS_ACTION_MOVE_OUTSIDE_BOUNDARY = 2;
const int STATUS_ACTION_MOVE_HIT_ANOTHER_ROBOT_ALONG_PATH = 3;

// Weapon: for the hit action
const int WEAPON_HIT_DAMAGE = 200;
const int WEAPON_HIT_RANGE = 1;

// Weapon: for the shoot action
const int WEAPON_SHOOT_DAMAGE = 100;
const int WEAPON_SHOOT_RANGE = 5;

const int STATUS_ACTION_WEAPON_NOT_IMPLEMENTED = 0;
const int STATUS_ACTION_WEAPON_SUCCESS = 1;
const int STATUS_ACTION_WEAPON_FAIL = 2;

int robotLetterToArrayIndex(const char robotLetter)
{
    return int(robotLetter - 'A');
}

char arrayIndexToRobotLetter(const int index)
{
    return char(index + 'A');
}

char actionTextToLetter(const char actionText[MAX_ACTION_TEXT_LENGTH])
{

    // In this game, only 3 possible values
    if (strcmp(actionText, ACTION_MOVE_TEXT) == 0)
    {
        return ACTION_MOVE;
    }
    else if (strcmp(actionText, ACTION_HIT_TEXT) == 0)
    {
        return ACTION_HIT;
    }
    else if (strcmp(actionText, ACTION_SHOOT_TEXT) == 0)
    {
        return ACTION_SHOOT;
    }
    return ACTION_ERROR;
}

char directionTextToLetter(const char directionText[MAX_DIRECTION_TEXT_LENGTH])
{
    // In this game, only 4 possible directions
    if (strcmp(directionText, DIRECTION_EAST_TEXT) == 0)
    {
        return DIRECTION_EAST;
    }
    else if (strcmp(directionText, DIRECTION_SOUTH_TEXT) == 0)
    {
        return DIRECTION_SOUTH;
    }
    else if (strcmp(directionText, DIRECTION_WEST_TEXT) == 0)
    {
        return DIRECTION_WEST;
    }
    else if (strcmp(directionText, DIRECTION_NORTH_TEXT) == 0)
    {
        return DIRECTION_NORTH;
    }
    return DIRECTION_ERROR;
}

const char *letterToDirectionText(char direction)
{
    if (direction == DIRECTION_EAST)
        return DIRECTION_EAST_TEXT;
    else if (direction == DIRECTION_SOUTH)
        return DIRECTION_SOUTH_TEXT;
    else if (direction == DIRECTION_WEST)
        return DIRECTION_WEST_TEXT;
    else if (direction == DIRECTION_NORTH)
        return DIRECTION_NORTH_TEXT;
    return DIRECTION_ERROR_TEXT;
}

void initializeMap(char map[MAX_ROWS][MAX_COLS], const int numRows, const int numCols)
{
    int r, c;
    for (r = 0; r < numRows; r++)
        for (c = 0; c < numCols; c++)
            map[r][c] = CHAR_EMPTY;
}

void initializeHealthPoints(int healthPoints[MAX_NUM_ROBOTS])
{
    int i;
    for (i = 0; i < MAX_NUM_ROBOTS; i++)
        healthPoints[i] = 0;
}

void readInputMap(char map[MAX_ROWS][MAX_COLS], int &mapRows, int &mapCols)
{
    int r, c;
    char line[MAX_COLS + 1]; // character array to store each line

    // Read the game map
    cin >> mapRows >> mapCols;
    initializeMap(map, mapRows, mapCols);

    cin.ignore(); // ignore the end line character in this line
    for (r = 0; r < mapRows; r++)
    {
        cin.getline(line, MAX_COLS + 1);
        for (c = 0; c < mapCols; c++)
            map[r][c] = line[c];
    }
}
void readInputHealthPoints(int healthPoints[MAX_NUM_ROBOTS])
{
    int numRobots, hp, i;
    char robotLetter;

    initializeHealthPoints(healthPoints);
    // Read robot letters and health points
    cin >> numRobots;
    for (i = 0; i < numRobots; i++)
    {
        cin >> robotLetter >> hp;
        // cout << robotLetter << hp << endl;
        healthPoints[robotLetterToArrayIndex(robotLetter)] = hp;
    }
}

void displayMap(const char map[MAX_ROWS][MAX_COLS], const int mapRows, const int mapCols)
{
    int r, c;
    for (r = 0; r < mapRows; r++)
    {
        for (c = 0; c < mapCols; c++)
            cout << map[r][c] << " ";
        cout << endl;
    }
}

void displayHealthPoints(const int healthPoints[MAX_NUM_ROBOTS])
{
    int i, hp;
    for (i = 0; i < MAX_NUM_ROBOTS; i++)
    {
        hp = healthPoints[i];
        if (hp > 0)
        {
            cout << "Robot " << arrayIndexToRobotLetter(i) << " HP=" << hp << endl;
        }
    }
}

bool findRobotInMap(const char map[MAX_ROWS][MAX_COLS],
                    const int mapRows,
                    const int mapCols,
                    char letter, int &row, int &col)
{

    int r, c;
    for (r = 0; r < mapRows; r++)
        for (c = 0; c < mapCols; c++)
            if (map[r][c] == letter)
            {
                row = r;
                col = c;
                return true;
            }
    return false;
}

bool isInsideMap(const int mapRows, const int mapCols, int row, int col)
{
    return row >= 0 && col >= 0 && row < mapRows && col < mapCols;
}

// Helper function for better code organization
int updateHealthPointsForWeapon(int healthPoints[MAX_NUM_ROBOTS],
                                char map[MAX_ROWS][MAX_COLS],
                                const int mapRows, const int mapCols,
                                const char robotLetter,
                                const char directionLetter,
                                const int weaponDamage,
                                const int weaponRange,
                                char &targetRobotLetter,
                                int &targetOriginalHealthPoint,
                                int &targetUpdatedHealthPoint)
{

    int curRow, curCol;
    int deltaRow, deltaCol;
    int newRow, newCol;
    int foundRow, foundCol;
    int targetArrayIndex;

    int curRange = 0;

    if (findRobotInMap(map, mapRows, mapCols, robotLetter, foundRow, foundCol))
    {
        curRow = foundRow;
        curCol = foundCol;

        deltaRow = deltaCol = 0;
        switch (directionLetter)
        {
        case DIRECTION_EAST:
            deltaCol = 1;
            break;
        case DIRECTION_WEST:
            deltaCol = -1;
            break;
        case DIRECTION_NORTH:
            deltaRow = -1;
            break;
        case DIRECTION_SOUTH:
            deltaRow = 1;
            break;
        } // end switch

        // Keep moving the block based on the direction
        while (true)
        {

            newRow = curRow + deltaRow;
            newCol = curCol + deltaCol;
            curRange = curRange + 1;

            if (isInsideMap(mapRows, mapCols, newRow, newCol))
            {

                // hits another robot along the path
                if ((map[newRow][newCol] >= 'A' && map[newRow][newCol] <= 'Z') && curRange <= weaponRange)
                {

                    // update the pass by reference variables
                    targetRobotLetter = map[newRow][newCol];
                    targetArrayIndex = robotLetterToArrayIndex(targetRobotLetter);
                    targetOriginalHealthPoint = healthPoints[targetArrayIndex];

                    targetUpdatedHealthPoint = targetOriginalHealthPoint - weaponDamage;
                    if (targetUpdatedHealthPoint <= 0)
                    {
                        map[newRow][newCol] = CHAR_EMPTY;
                        targetUpdatedHealthPoint = 0;
                    }
                    healthPoints[targetArrayIndex] = targetUpdatedHealthPoint;
                    return STATUS_ACTION_WEAPON_SUCCESS;
                }

                if (curRange > weaponRange)
                {
                    return STATUS_ACTION_WEAPON_FAIL; // cannot hit the target, outside the range
                }

                curRow = newRow;
                curCol = newCol;
            }
            else
            {
                return STATUS_ACTION_WEAPON_FAIL; // cannot hit the target, outside the boundary
            }
        }
    }

    return STATUS_ACTION_WEAPON_NOT_IMPLEMENTED;
}

// TODO:
int updateHealthPointsForHitAction(int healthPoints[MAX_NUM_ROBOTS],
                                   char map[MAX_ROWS][MAX_COLS],
                                   const int mapRows, const int mapCols,
                                   const char robotLetter,
                                   const char directionLetter,
                                   char &targetRobotLetter,
                                   int &targetOriginalHealthPoint,
                                   int &targetUpdatedHealthPoint)
{

    // Call the common helper function with a generalized logic
    return updateHealthPointsForWeapon(healthPoints,
                                       map, mapRows, mapCols,
                                       robotLetter,
                                       directionLetter,
                                       WEAPON_HIT_DAMAGE,
                                       WEAPON_HIT_RANGE,
                                       targetRobotLetter,
                                       targetOriginalHealthPoint,
                                       targetUpdatedHealthPoint);

    // return STATUS_ACTION_WEAPON_NOT_IMPLEMENTED;
}

// TODO:
int updateHealthPointsForShootAction(int healthPoints[MAX_NUM_ROBOTS],
                                     char map[MAX_ROWS][MAX_COLS],
                                     const int mapRows, const int mapCols,
                                     const char robotLetter,
                                     const char directionLetter,
                                     char &targetRobotLetter,
                                     int &targetOriginalHealthPoint,
                                     int &targetUpdatedHealthPoint)
{

    // Call the common helper function with a generalized logic
    return updateHealthPointsForWeapon(healthPoints,
                                       map, mapRows, mapCols,
                                       robotLetter,
                                       directionLetter,
                                       WEAPON_SHOOT_DAMAGE,
                                       WEAPON_SHOOT_RANGE,
                                       targetRobotLetter,
                                       targetOriginalHealthPoint,
                                       targetUpdatedHealthPoint);

    // return STATUS_ACTION_WEAPON_NOT_IMPLEMENTED;
}

// TODO:
int updateMapForMoveAction(char map[MAX_ROWS][MAX_COLS], const int mapRows, const int mapCols,
                           const char robotLetter, const char directionLetter, const int moveSteps)
{

    int curRow, curCol;
    int deltaRow, deltaCol;
    int newRow, newCol;
    int foundRow, foundCol;
    int curSteps = moveSteps;

    if (findRobotInMap(map, mapRows, mapCols, robotLetter, foundRow, foundCol))
    {
        curRow = foundRow;
        curCol = foundCol;

        deltaRow = deltaCol = 0;
        switch (directionLetter)
        {
        case DIRECTION_EAST:
            deltaCol = 1;
            break;
        case DIRECTION_WEST:
            deltaCol = -1;
            break;
        case DIRECTION_NORTH:
            deltaRow = -1;
            break;
        case DIRECTION_SOUTH:
            deltaRow = 1;
            break;
        } // end switch

        // Keep moving the block based on the direction
        while (true)
        {

            newRow = curRow + deltaRow;
            newCol = curCol + deltaCol;

            if (isInsideMap(mapRows, mapCols, newRow, newCol))
            {

                // hits another robot along the path?
                if ((map[newRow][newCol] >= 'A' && map[newRow][newCol] <= 'Z'))
                {

                    // restore the robot to the original position
                    map[curRow][curCol] = CHAR_EMPTY;
                    map[foundRow][foundCol] = robotLetter;

                    return STATUS_ACTION_MOVE_HIT_ANOTHER_ROBOT_ALONG_PATH;
                }
                else
                {
                    // keep moving the robot
                    map[curRow][curCol] = CHAR_EMPTY;
                    map[newRow][newCol] = robotLetter;
                    curRow = newRow;
                    curCol = newCol;

                    curSteps = curSteps - 1;
                    if (curSteps == 0)
                    {
                        return STATUS_ACTION_MOVE_SUCCESS;
                    }
                }
            }
            else
            {
                // restore the robot to the original position
                map[curRow][curCol] = CHAR_EMPTY;
                map[foundRow][foundCol] = robotLetter;

                // cannot move outside the map
                return STATUS_ACTION_MOVE_OUTSIDE_BOUNDARY;
            }
        }
    }

    return STATUS_ACTION_MOVE_NOT_IMPLMENTED;
}

/**
 * function: the main function
 *
 * Note: The main function is given. Do not modify anything inside
 */
int main()
{
    char map[MAX_ROWS][MAX_COLS];
    int healthPoints[MAX_NUM_ROBOTS];

    int mapRows, mapCols, moveSteps;
    int statusMove, statusHit, statusShoot;
    char robotLetter, actionLetter, directionLetter;
    char actionText[MAX_ACTION_TEXT_LENGTH];
    char directionText[MAX_DIRECTION_TEXT_LENGTH];

    char targetRobotLetter;
    int targetOriginalHealthPoint;
    int targetUpdatedHealthPoint;

    // Start by reading the input
    // Usage:
    // ./pa1 < testcase/inputXX.txt
    readInputHealthPoints(healthPoints);
    readInputMap(map, mapRows, mapCols);

    cout << "The initial game information:" << endl;
    displayHealthPoints(healthPoints);
    displayMap(map, mapRows, mapCols);

    while (true)
    {
        cin >> robotLetter;
        if (robotLetter == CHAR_END_INPUT)
            break; // End of the game

        // if the robot letter is not the end of the game
        // read the action text and the direction letter
        cin >> actionText >> directionText;
        actionLetter = actionTextToLetter(actionText);
        directionLetter = directionTextToLetter(directionText);
        if (actionLetter == ACTION_MOVE)
        {

            // need to read the steps if the action is ACTION_MOVE
            cin >> moveSteps;

            // debug:
            // cout << robotLetter << " " << actionLetter << " " << directionLetter << " " << moveSteps << endl;

            statusMove = updateMapForMoveAction(map, mapRows, mapCols, robotLetter, directionLetter, moveSteps);

            if (statusMove == STATUS_ACTION_MOVE_NOT_IMPLMENTED)
            {
                cout << "The move action is not implemented yet" << endl;
            }
            else if (statusMove == STATUS_ACTION_MOVE_SUCCESS)
            {
                cout << "Success: "
                     << "Robot " << robotLetter << " moves along the direction " << letterToDirectionText(directionLetter) << " by " << moveSteps << " step(s)" << endl;
                displayMap(map, mapRows, mapCols);
            }
            else if (statusMove == STATUS_ACTION_MOVE_OUTSIDE_BOUNDARY)
            {
                cout << "Fail: "
                     << "If robot " << robotLetter << " moves along the direction " << letterToDirectionText(directionLetter) << " by " << moveSteps << " step(s)"
                     << ", it will move outside a boundary, so the position remains unchanged" << endl;
                displayMap(map, mapRows, mapCols);
            }
            else if (statusMove == STATUS_ACTION_MOVE_HIT_ANOTHER_ROBOT_ALONG_PATH)
            {
                cout << "Fail: "
                     << "If robot " << robotLetter << " moves along the direction " << letterToDirectionText(directionLetter) << " by " << moveSteps << " step(s)"
                     << ", it will hit another robot along the path, so the position remains unchanged" << endl;
                displayMap(map, mapRows, mapCols);
            }
        }
        else if (actionLetter == ACTION_HIT)
        {

            // debug:
            // cout << robotLetter << " " << actionLetter << " " << directionLetter <<  endl;
            statusHit = updateHealthPointsForHitAction(healthPoints, map, mapRows, mapCols, robotLetter, directionLetter, targetRobotLetter, targetOriginalHealthPoint, targetUpdatedHealthPoint);
            if (statusHit == STATUS_ACTION_WEAPON_NOT_IMPLEMENTED)
            {
                cout << "The hit action is not implemented yet" << endl;
            }
            else if (statusHit == STATUS_ACTION_WEAPON_SUCCESS)
            {

                cout << "Success: "
                     << "Robot " << robotLetter << " hits " << targetRobotLetter << endl;
                cout << "Robot " << targetRobotLetter << " health point is reduced from " << targetOriginalHealthPoint << " to " << targetUpdatedHealthPoint << endl;
                if (targetUpdatedHealthPoint == 0)
                {
                    cout << "Robot " << targetRobotLetter << " is being destroyed by " << robotLetter << endl;
                    displayMap(map, mapRows, mapCols);
                }
                cout << "== Health points of alive robots ==" << endl;
                displayHealthPoints(healthPoints);
            }
            else if (statusHit == STATUS_ACTION_WEAPON_FAIL)
            {

                cout << "Fail: "
                     << "Robot " << robotLetter << " cannot hit any target" << endl;
                cout << "== Health points of alive robots ==" << endl;
                displayHealthPoints(healthPoints);
            }
        }
        else if (actionLetter == ACTION_SHOOT)
        {

            // debug:
            // cout << robotLetter << " " << actionLetter << " " << directionLetter <<  endl;
            statusShoot = updateHealthPointsForShootAction(healthPoints, map, mapRows, mapCols, robotLetter, directionLetter, targetRobotLetter, targetOriginalHealthPoint, targetUpdatedHealthPoint);
            if (statusShoot == STATUS_ACTION_WEAPON_NOT_IMPLEMENTED)
            {
                cout << "The shoot action is not implemented yet" << endl;
            }
            else if (statusShoot == STATUS_ACTION_WEAPON_SUCCESS)
            {

                cout << "Success: "
                     << "Robot " << robotLetter << " shoots " << targetRobotLetter << endl;
                cout << "Robot " << targetRobotLetter << " health point is reduced from " << targetOriginalHealthPoint << " to " << targetUpdatedHealthPoint << endl;
                if (targetUpdatedHealthPoint == 0)
                {
                    cout << "Robot " << targetRobotLetter << " is being destroyed by " << robotLetter << endl;
                    displayMap(map, mapRows, mapCols);
                }
                cout << "== Health points of alive robots ==" << endl;
                displayHealthPoints(healthPoints);
            }
            else if (statusShoot == STATUS_ACTION_WEAPON_FAIL)
            {

                cout << "Fail: "
                     << "Robot " << robotLetter << " cannot shoot any target" << endl;
                cout << "== Health points of alive robots ==" << endl;
                displayHealthPoints(healthPoints);
            }
        }
    }
    cout << "=== Game Ended ===" << endl;

    return 0;
}
#include <iostream>
#include <iomanip>
#include <cstring>

using namespace std;

const int MAX_PLAYER_NAME = 10;

class LinkNode
{
private:
    float score;
    char *name;
    LinkNode *prev; // point to previous node
    LinkNode *next; // point to next node

public:
    char *getName()
    {
        return name;
    }
    float getScore()
    {
        return score;
    }
    LinkNode *getPrev()
    {
        return prev;
    };
    LinkNode *getNext()
    {
        return next;
    };
    void setPrev(LinkNode *prev)
    {
        this->prev = prev;
    }
    void setNext(LinkNode *next)
    {
        this->next = next;
    }
    void show()
    {
        cout << left << setw(10) << name << left << setw(10) << score;
    }

    // Task 1: Complete the Constructor and Destructor function
    // tips: allocate and release variable with dynamic memory
    // Constructor
    LinkNode(char *name, float score)
    {
        this->name = new char[MAX_PLAYER_NAME];
        strcpy(this->name, name);
        this->score = score;
        this->prev = nullptr;
        this->next = nullptr;
    }
    // Destructor
    ~LinkNode()
    {
        delete[] name;
    }
};

class DoubledLink
{
private:
    LinkNode *head; // point to the head node
    LinkNode *tail; // point to the tail node

private:
    // Task 2: Complete the insert function: insert Node a in the front of Node b
    // tips: check the boundary condition, e.g. Node a/b/tail is nullptr
    void insert(LinkNode *newNode, LinkNode *existNode)
    {
        if (newNode == nullptr)
        {
            return;
        }
        if (tail == nullptr)
        { // DoubledLink is null
            head = newNode;
            tail = newNode;
            return;
        }
        if (existNode == nullptr)
        { // insert at the tail of DoubledLink
            tail->setNext(newNode);
            newNode->setPrev(tail);
            newNode->setNext(nullptr);
            tail = newNode;
        }
        else
        {
            newNode->setPrev(existNode->getPrev());
            newNode->setNext(existNode);
            if (existNode->getPrev() != nullptr)
            {
                existNode->getPrev()->setNext(newNode);
            }
            else
            {
                head = newNode;
            }
            existNode->setPrev(newNode);
        }
    }

    // Task 3: Complete the remove function: remove Node in DoubledLink, if Node is nullptr, return void
    // tips: check the boundary condition, e.g. Node is nullptr/head/tail
    void remove(LinkNode *node)
    {
        // Remove Node, if it is nullptr, return without any action.
        if (node == nullptr)
        {
            // Invalid player node
            return;
        }
        if (node == head)
        {
            // If the player is the head, update the head
            head = node->getNext();
        }
        if (node == tail)
        {
            // If the player is the tail, update the tail
            tail = node->getPrev();
        }
        if (node->getPrev() != nullptr)
        {
            // Update the previous node's next pointer
            node->getPrev()->setNext(node->getNext());
        }
        if (node->getNext() != nullptr)
        {
            // Update the next node's previous pointer
            node->getNext()->setPrev(node->getPrev());
        }

        delete node;
    }

    /* YOU MUST NOT MODIFY PUBLIC FUNCTIONS BELOW, EXCEPT CONSTRUCTOR & DECONSTRUCTOR */
public:
    LinkNode *queryName(char *targetname)
    {
        LinkNode *curNode = head;
        while (curNode != nullptr)
        {
            if (strcmp(curNode->getName(), targetname) == 0)
            {
                return curNode;
            }
            curNode = curNode->getNext();
        }
        return nullptr;
    }
    LinkNode *queryBelowScore(float targetScore)
    {
        LinkNode *curNode = head;
        while (curNode != nullptr)
        {
            if (curNode->getScore() < targetScore)
            {
                return curNode;
            }
            curNode = curNode->getNext();
        }
        return nullptr;
    }
    void addPlayer(char *name, float score)
    {
        LinkNode *queryPlayer = this->queryName(name);
        if (queryPlayer != nullptr)
            this->remove(queryPlayer); // find existed player

        LinkNode *newPlayer = new LinkNode(name, score); // set Node in LinkNode
        LinkNode *insertPlayer = this->queryBelowScore(score);
        this->insert(newPlayer, insertPlayer);
    }
    void show()
    {
        LinkNode *curNode = head;
        int rank = 1;
        cout << "================ Game Leaderboard ==============" << endl;
        cout << "Rank  Name  Score" << endl;
        while (curNode != nullptr)
        {
            cout << rank << " ";
            curNode->show();
            cout << " " << endl;
            curNode = curNode->getNext();
            rank++;
        }
    }
    /* YOU MUST NOT MODIFY FUNCTIONS ABOVE, EXCEPT CONSTRUCTOR & DECONSTRUCTOR */

public:
    // Task 4: Complete the Constructor and Destructor function
    // Constructor
    DoubledLink()
    {
        head = nullptr;
        tail = nullptr;
    }
    // Destructor
    ~DoubledLink()
    {
        while (head != nullptr)
        {
            LinkNode *temp = head;
            head = head->getNext();
            delete temp;
        }
    }
};

/* YOU MUST NOT MODIFY THE MAIN FUNCTION BELOW */
int main()
{
    DoubledLink *gameLeaderboard = new DoubledLink();
    cout << "This is a real-time updated game leaderboard, players ranked in descending order by score." << endl;
    cout << "Some new players join, some players update score." << endl;
    cout << "Game Ranking will show after each operation." << endl;
    cout << "Game over when input 0 0." << endl;

    while (true)
    {
        char name[MAX_PLAYER_NAME]; // Declare the Player's name
        float score;                // Declare the Player's score
        cin >> name >> score;
        if (strcmp(name, "0") == 0 && score == 0)
        {
            cout << "Game Over." << endl;
            break;
        }
        // update game leaderboard
        gameLeaderboard->addPlayer(name, score);
        gameLeaderboard->show();
    }

    delete gameLeaderboard;
    return 0;
}

/*************************************************************************
	> File Name: MazeFactory.cpp
	> Author: 
	> Mail: 
	> Created Time: 2017年03月12日 星期日 17时49分07秒
 ************************************************************************/

#include<iostream>
using namespace std;

class MazeFactory{
  public:
  MazeFactory();

  virtual Maze* MakeMaze() const
  {
    return new Maze;
  }
  virtual Wall* MakeWall() const
  {
    return new Wall;
  }
  virtual Room* MakeRoom(int n) const
  {
    return new Room(n);
  }
  virtual Door* MakeDoor(Room* r1, Room* r2) const
  {
    return new Door(r1, r2);
  }
};


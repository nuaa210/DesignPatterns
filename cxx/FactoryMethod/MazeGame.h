/*************************************************************************
	> File Name: MazeGame.h
	> Author: 
	> Mail: 
	> Created Time: 2017年02月01日 星期三 09时36分33秒
 ************************************************************************/

#ifndef _MAZEGAME_H
#define _MAZEGAME_H

class MazeGame{
public:
    Maze* CreateMaze();

    // factory methods:
    virtual Maze* MakeMaze() const
    {
        return new Maze;
    }
    virtual Room* MakeRoom(int n) const
    {
        return new Room(n);
    }
    virtual Wall* MakeWall() const
    {
        return new Wall;
    }
    virtual Door* MakeDoor(Room* r1 Room* r2) const
    {
        return new Door(r1, r2);
    }
}
#endif

/*************************************************************************
	> File Name: BombedMazeGame.h
	> Author: 
	> Mail: 
	> Created Time: 2017年02月01日 星期三 09时48分54秒
 ************************************************************************/

#ifndef _BOMBEDMAZEGAME_H
#define _BOMBEDMAZEGAME_H

class BombedMazeGame:public MazeGame{
public:
    BombedMazeGame();

    virtual Wall* MakeWall() const
    {
        return new BombedWall;
    }
    virtual Room* MakeRoom(int n) const
    {
        return new RoomWithABomb(n);
    }
}
#endif

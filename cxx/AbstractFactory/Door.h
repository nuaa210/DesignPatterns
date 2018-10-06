/*************************************************************************
	> File Name: Door.h
	> Author: 
	> Mail: 
	> Created Time: 2017年01月31日 星期二 10时48分18秒
 ************************************************************************/

#ifndef _DOOR_H
#define _DOOR_H

class Door: public MapSite{
public:
    Door(Room* = 0, Room* = 0);

    virtual void Enter();
    Room* otherSideFrom(Room*);

private:
    Room* _room1;
    Room* _room2;
    bool _isOpen;
};
#endif

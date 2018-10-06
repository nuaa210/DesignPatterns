/*************************************************************************
	> File Name: Room.h
	> Author: 
	> Mail: 
	> Created Time: 2017年01月31日 星期二 10时42分37秒
 ************************************************************************/

#ifndef _ROOM_H
#define _ROOM_H

class Room:public MapSite {
    public:
    Room(int roomNo);

    MapSite* GetSide(Direction) const;
    void SetSide(Direction, MapSite*);

    virtual void Enter();

private:
    MapSite* _sides[4];
    int _roomNumber;
};
#endif

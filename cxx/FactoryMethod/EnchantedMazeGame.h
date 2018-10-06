/*************************************************************************
	> File Name: EnchantedMazeGame.h
	> Author: 
	> Mail: 
	> Created Time: 2017年02月01日 星期三 09时51分17秒
 ************************************************************************/

#ifndef _ENCHANTEDMAZEGAME_H
#define _ENCHANTEDMAZEGAME_H

class EnchantedMazeGame: public MazeGame{
public:
    EnchantedMazeGame();

    virtual Room* MakeRoom(int n)const
    {

        return new EnchantedRoom(n, CastSpell());
    }
    virtual Door* MakeDoor(Room* r1, Room* r2) const
    {
        return new DoorNeedingSpell(r1, r2);
    }
protected:
    Spell* CastSpell() const;
};
#endif

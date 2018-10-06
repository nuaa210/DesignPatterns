/*************************************************************************
	> File Name: MapSite.h
	> Author: 
	> Mail: 
	> Created Time: 2017年01月31日 星期二 10时41分14秒
 ************************************************************************/

#ifndef _MAPSITE_H
#define _MAPSITE_H

enum Direction {North, South, East, West};

class MapSite {
public:
    virtual void Enter()=0;
};


#endif

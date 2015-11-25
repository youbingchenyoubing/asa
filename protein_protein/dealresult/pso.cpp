 #include <iostream>  
#include <cmath>  
#include <cstdlib>  
using namespace std;  
 
#define C1 2  
#define C2 2  
#define VMAX 5.0  
#define MAX_ITERATIONS 100  
float rand01()  
{  
        return (float) (rand()/(double)RAND_MAX);  
}  
struct particle{  
        float current;  
        float pbest;  
};  
 
float fitness(float x)  
{  
        return x*x - 20*x + 100;  
}  
 
float gbest = 10000;  
struct particle p[5];  
float v[5] = {0};  
 
void init_particles()  
{  
        int i;  
        for(i = 0; i < 5; i++)  
        {  
                p[i].current = -2+i;  
                p[i].pbest = p[i].current;  
        }  
}  
void find_gbest()  
{  
        int i;  
        for(i = 0; i < 5; i++)  
        {  
                        if(fitness(gbest) > fitness(p[i].current))  
                                gbest = p[i].current;  
        }  
}  
void adjust_v()  
{  
        int i ;  
        for(i = 0; i < 5; i++)  
        {  
                v[i] = v[i] + C1*rand01()*(p[i].pbest - p[i].current) + C2*rand01()*(gbest - p[i].current);  
                if(v[i] > VMAX)  
                        v[i] = VMAX;  
        }  
}  
void pso()  
{  
        int i,iter_num;  
        iter_num = 1;  
        while(iter_num < MAX_ITERATIONS)  
        {  
                /*for(i = 0; i < 5; i++)  
                {  
                        cout <<"p"<<i<<":current "<<p[i].current<<" pbest "<<p[i].pbest<<endl;  
                }  
                cout <<"gbest:"<<gbest<<endl;  
                cout <<endl;  
                getchar();*/ 
                for(i = 0; i < 5; i++)  
                {  
                        if(fitness(p[i].current) < fitness(p[i].pbest))  
                                p[i].pbest = p[i].current;  
                }  
                find_gbest();  
                adjust_v();  
                for(i = 0; i < 5; i++)  
                        p[i].current += v[i];  
                iter_num ++;  
        }  
}  
int main()  
{  
 
        init_particles();  
        pso();  
        printf("After %d iterations,gbest is %f\n",MAX_ITERATIONS,gbest);  
        return 0;  
}  

#include <stdlib.h>
#include "MLX42/MLX42.h"
#include <Python.h>

bool my_keyhook(mlx_key_data_t keydata, void* param)
{
		if (keydata.key != NULL)
            system("pmset displaysleepnow")
        else
            return(0);
}


//https://github.com/arommers/so_long/blob/7b8bbc712db125d816a97a21c6acc1dc8e15c476/MLX42/main.c

int32_t	main(void)
{
    while(1)
	    mlx_key_hook(NULL, &my_keyhook, NULL);
    return(0);
	
}
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <fcntl.h>
#include <termios.h>
#include <sys/ioctl.h>
#include <errno.h>
#include <linux/fb.h>
#include <sys/mman.h>

#define FB_PATH "/dev/fb0"
int main( int argc, char **argv )
{
  int size;
  char r, g, b;
  int x,y;
  void* buffer;
  int fd;
  int (*m)[1280];
  int *p;
  int fd_out;
  struct fb_fix_screeninfo fix_info;
  struct fb_var_screeninfo var_info;
  
  fd = open(FB_PATH, O_RDWR);
  if(fd < 0) {
    printf("Unable to open\n");
    return 1;
  }

  if(ioctl(fd, FBIOGET_FSCREENINFO, &fix_info) < 0) {
    printf("get fixed screen info failed: %s\n", strerror(errno));
    close(fd);
    return 1;
  }

  if(ioctl(fd, FBIOGET_VSCREENINFO, &var_info) < 0) {
    printf("get variable screen info failed: %s\n", strerror(errno));
    close(fd);
    return 1;
  }  

  printf("Screen resolution: (%dx%d)\n", var_info.xres, var_info.yres);
  printf("Line width in bytes %d\n", fix_info.line_length);
  printf("bits per pixel : %d\n", var_info.bits_per_pixel);
  printf("Red: length %d bits, offset %d\n", var_info.red.length, var_info.red.offset);
  printf("Grren: length %d bits, offset %d\n", var_info.green.length, var_info.green.offset);
  printf("Blue: length %d bits, offset %d\n", var_info.blue.length, var_info.blue.offset);

  //draw
  size = fix_info.line_length * var_info.yres;
  
  buffer = mmap(NULL, size, PROT_READ | PROT_WRITE, MAP_SHARED, fd, 0);
  if(!buffer){
    printf("mmap failed\n");
    close(fd);
    return 1;
  }

  p = buffer;

  for(x=0; x<100; x++)
    printf("%x, ",p[x]);
  putchar('\n');

 /* 
  for(x=0; x<1280*800; x++){
    p[x] |= 0xff000000;
  }
*/
  printf("size= %d\n", var_info.xres * var_info.yres * 4); 
  fd_out = open("fb_dump.raw", O_WRONLY);
  for(x=0; x< var_info.xres * var_info.yres; x++){
    write(fd_out, &(p[x]), 4);
  }

/*
  m = buffer;
  for(y=0;y< 100; y++)
    for(x=0;x<100;x++){
      int* p = &(m[y]);
      p[x] = 0xffffffff;  //white
    }
  for(y=101;y< 200; y++)
    for(x=0;x<100;x++){
      int* p = &(m[y]);
      p[x] = 0xffff0000;  //red
    }
  for(y=201;y< 300; y++)
    for(x=0;x<100;x++){
      int* p = &(m[y]);
      p[x] = 0xff00ff00;  //green
    }
  for(y=301;y< 400; y++)
    for(x=0;x<100;x++){
      int* p = &(m[y]);
      p[x] = 0xff0000ff;  //blue
    }
  for(y=401;y< 500; y++)
    for(x=0;x<100;x++){
      int* p = &(m[y]);
      p[x] = 0x44FF0000;
    }  
  for(y=501;y< 600; y++)
    for(x=0;x<100;x++){
      int* p = &(m[y]);
      p[x] = 0x00FF0000;
    } 

*/
    
  munmap(buffer, 0);

  
    
  
  close(fd_out);
  close(fd);
  return 0;
} 

##########################################################################
# File Name: png2jpg.sh
# Author: LiYingying
# mail: yingyinglee@163.com
# Created Time: 2019年11月12日 星期二 14时47分17秒
#########################################################################


find kitti/ -name '*.png' | parallel 'convert -quality 92 -sampling-factor 2x2,1x1,1x1 {.}.png {.}.jpg && rm {}'

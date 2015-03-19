#Pepperレポジトリ

###環境
Python : 2.7.6

###参考
#####ソースコード参照
- [Making NAO move and speak](https://community.aldebaran-robotics.com/doc/2-0/dev/python/making_nao_move.html)
- [Poses](https://community.aldebaran-robotics.com/doc/2-0/dev/python/examples/motion/poses.html?highlight=ptargetangles)

#####pepper仕様
[Pepper - Joints](https://community.aldebaran-robotics.com/doc/2-0/family/juliette_technical/joints_juliette.html)

##talk.py
pepperの両腕を`Stand`状態にした後、`Zero`の状態に持ってゆく。  
ただし、これはposeを決めたわけではなく、直接値を設定することにより実現している。


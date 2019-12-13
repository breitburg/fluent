pip3 install https://github.com/libfluent/fluent.git

wget http://www.ferzkopp.net/Software/SDL2_gfx/SDL2_gfx-1.0.4.zip
unzip SDL2_gfx-1.0.4.zip
cd SDL2_gfx-1.0.4

./configure
make
make install

cd ..
wget https://www.libsdl.org/projects/SDL_ttf/release/SDL2_ttf-2.0.15.zip
unzip SDL2_ttf-2.0.15.zip
cd SDL2_ttf-2.0.15

./configure
make
make install

echo 'Done!'

rm -fr SDL2_ttf-2.0.15.zip SDL2_ttf-2.0.15 SDL2_gfx-1.0.4.zip SDL2_gfx-1.0.4
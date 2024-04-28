CC = clang
BIN = bin
SRC = $(wildcard *.c)
OBJ = $(SRC:.c=.o)

all: clean build

build: $(OBJ)
	$(CC) -o $(BIN)/sort $^

run: all 
	$(BIN)/sort

clean:
	rm $(BIN)/sort
	rm *.o

init:
	mkdir -p $(BIN)
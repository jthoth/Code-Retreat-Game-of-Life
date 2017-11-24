import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation

class GameOfLife(object):

    def __init__(self, **kwargs):
        self.figure, self.axis = plt.subplots()
        self.on = 255
        self.off = 0

    def __random_grid(self, n):
        return np.random.choice([self.off,self.on], n*n, p=[0.3, 0.7]).reshape(n, n)

    def compute_total(self, grid, i , j, n):
        return int((grid[i, (j-1)%n] + grid[i, (j+1)%n] +
                    grid[(i-1)%n, j] + grid[(i+1)%n, j] +
                    grid[(i-1)%n, (j-1)%n] + grid[(i-1)%n, (j+1)%n] +
                    grid[(i+1)%n, (j-1)%n] + grid[(i+1)%n, (j+1)%n])/255)

    def __survive(self, new_grid, grid, i , j, total):
        if grid[i, j]  == self.on and ((total < 2) or (total > 3)):
            new_grid[i, j] = self.off
        return new_grid

    def __die(self, new_grid, grid, i , j, total):
        if grid[i, j]  == self.off and total == 3:
            new_grid[i, j] = self.on
        return new_grid

    def survive_or_die(self, new_grid, grid, i , j, total ):
        new_grid = self.__survive(new_grid, grid, i , j, total)
        new_grid = self.__die(new_grid, grid, i , j, total)
        return new_grid

    def __copy_result(self, image, new_grid, grid):
        image.set_data(new_grid)
        grid[:] = new_grid[:]
        return image

    def __update(self,image, new_grid, grid, n):
        for i in range(n):
            for j in range(n):
                self.survive_or_die(new_grid, grid, i, j, self.compute_total(grid, i, j, n))
        return self.__copy_result(image,new_grid, grid)

    def __preupdate(self, frame_number,image, grid, n):
        new_grid = grid.copy()
        return self.__update(image, new_grid, grid, n)

    def run_animation(self, n):
        grid = self.__random_grid(n)
        image = self.axis.imshow(grid)
        ani = animation.FuncAnimation(self.figure, self.__preupdate, fargs=(image,grid, n, ), interval=40)
        plt.show()

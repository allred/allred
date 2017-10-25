class MineSweeper
  attr_accessor :size, :num_mines, :mines_locations, :grid, :lost, :won

  def initialize(size: 4, num_mines: 1)
    @size = size
    @num_mines = num_mines
    @mines_locations = []
    @grid = []
    (1..@size).each do |_|
      @grid << Array.new(@size)
    end
    populate_mines(@num_mines)
    @lost = false
    @won = false
    @explosion = "\u{1f4a5}".encode('utf-8')
    @bomb = "\u{1f4a3}".encode('utf-8')
    @symbol_clear = ' '
    @symbol_mine = 'M'
  end

  def populate_mines(num_mines)
    mines_placed = 0
    until mines_placed.eql? num_mines
      row = rand(@size)
      col = rand(@size)
      unless @grid[row][col].eql? 'M'
        @mines_locations << [row, col]
        @grid[row][col] = 'M'
        mines_placed += 1
      end
    end
  end

  def uncover(v, h, vmax=@size, vmin=0, hmax=@size, hmin=0)
    abort "don't use this yet, it uncovers the whole board, a better way would be to scan the grid and clear all which have 0 adjacent mines"
    @grid[v][h] = @symbol_clear
    puts [uc: [v, h]]
    if v + 1 < vmax && grid[v+1][h] != @symbol_mine && grid[v+1][h] != @symbol_clear
       vmax = v if grid[v+1][h] == @symbol_mine
       uncover(v+1, h, vmax, vmin, hmax, hmin)
    end
    if v - 1 >= vmin && grid[v-1][h] != @symbol_mine && grid[v-1][h] != @symbol_clear
       vmin = v if grid[v-1][h] == @symbol_mine
       uncover(v-1, h, vmax, vmin, hmax, hmin)
    end
    if h + 1 < hmax && grid[v][h+1] != @symbol_mine && grid[v][h+1] != @symbol_clear
       uncover(v, h+1, vmax, vmin, hmax, hmin)
    end
    if h - 1 >= hmin && grid[v][h-1] != @symbol_mine && grid[v][h-1] != @symbol_clear
       uncover(v, h-1, vmax, vmin, hmax, hmin)
    end
  end

  def num_adjacent(v, h)
    num_adjacent = 0
    num_adjacent +=1 if @mines_locations.include?([v+1, h])
    num_adjacent +=1 if @mines_locations.include?([v-1, h])
    num_adjacent +=1 if @mines_locations.include?([v, h+1])
    num_adjacent +=1 if @mines_locations.include?([v, h-1])
    num_adjacent +=1 if @mines_locations.include?([v+1, h+1])
    num_adjacent +=1 if @mines_locations.include?([v+1, h-1])
    num_adjacent +=1 if @mines_locations.include?([v-1, h+1])
    num_adjacent +=1 if @mines_locations.include?([v-1, h-1])
    return num_adjacent
  end

  def play(v, h, type=nil)
    return if @lost
    @mines_locations.each do |coord|
      if coord.eql? [v, h]
        @grid[v][h] = @explosion
        @lost = true
      end
    end
    if !@lost
      num_adjacent = num_adjacent(v, h)
      @grid[v][h] = num_adjacent.to_s
    end
  end

  def display
    puts
    #die = "\u{1f3b2}".encode('utf-8')
    corner = " "
    puts ["#{corner}": @grid[0].each_with_index.map {|_, i| i.to_s }]
    @grid.each_with_index do |r, i|
      puts ["#{i}": r]
    end
  end

  def run
  end
end

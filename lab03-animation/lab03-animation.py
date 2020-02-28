import arcade

def draw_sea():
    """Dibujar mar"""
    arcade.draw_lrtb_rectangle_filled(0, 600, 250, 0, arcade.color.QUEEN_BLUE)

def draw_moon():
    """Dibujar luna"""
    arcade.draw_circle_filled(300, 450, 140, arcade.color.PLATINUM)

def draw_stars():
    """Dibujar estrellas"""
    arcade.draw_points([[50, 580], [90, 400], [100, 500], [40, 510], [60, 350]], arcade.color.AUREOLIN, 10)
    arcade.draw_points([[400, 580], [580, 550], [500, 400], [500, 500], [530, 350]], arcade.color.AUREOLIN, 10)

def draw_fish(x):
    """"Dibujar pez"""
    arcade.draw_ellipse_filled(100 + x, 200, 70, 30, arcade.color.ARSENIC)
    arcade.draw_triangle_filled(75 + x, 202, 40 + x, 220, 40 + x, 182, arcade.color.ARSENIC)
    arcade.draw_point(120 + x, 202, arcade.color.WHITE, 10)

def on_draw(delta_time):
    arcade.start_render()
    draw_sea()
    draw_moon()
    draw_stars()
    draw_fish(on_draw.fish1_x)
    on_draw.fish1_x +=5
on_draw.fish1_x=100

def main():
    arcade.open_window(600, 600, "Drawing Example")
    arcade.set_background_color(arcade.color.COOL_BLACK)

    arcade.schedule(on_draw, 1 / 60)
    arcade.run()

main()

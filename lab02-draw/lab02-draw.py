import arcade

arcade.open_window(600, 600, "Drawing Example")
arcade.set_background_color(arcade.color.COOL_BLACK)
arcade.start_render()

#Dibujar mar
arcade.draw_lrtb_rectangle_filled(0, 600, 250, 0, arcade.color.QUEEN_BLUE)

#Dibujar luna
arcade.draw_circle_filled(300,450,140,arcade.color.PLATINUM)

#Dibujar estrellas
arcade.draw_points([[50,580],[90,400],[100,500],[40,510],[60,350]],arcade.color.AUREOLIN,10)
arcade.draw_points([[400,580],[580,550],[500,400],[500,500],[530,350]],arcade.color.AUREOLIN,10)

#Dibujar pez
arcade.draw_ellipse_filled(100,200, 70, 30, arcade.color.ARSENIC)
arcade.draw_triangle_filled(75,202,40,220,40,182,arcade.color.ARSENIC)
arcade.draw_point(120,202,arcade.color.WHITE,10)

arcade.finish_render()
arcade.run()

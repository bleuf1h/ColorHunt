import flet as ft 
#Page setup
def main(page:ft.Page):
    page.title = "COLOR HUNT/RAINBOW MIXER"

    rgb_text = ft.Text("RGB:0, 0, 0", size = 30)

    def colorupdate(e):
        red = int(redslider.value)
        green = int(greenslider.value)
        blue = int(blueslider.value)

        hex_value = f"#{red:02x}{green:02x}{blue:02x}"
        page.bgcolor = hex_value

        rgb_text.value = f"RGB({red}, {green}, {blue})"
        page.update()

#Sliders

    redslider = ft.Slider(min = 0, max = 255, value = 0, on_change = colorupdate)
    greenslider = ft.Slider(min = 0, max = 255, value = 0, on_change = colorupdate)
    blueslider = ft.Slider(min = 0, max = 255, value = 0, on_change = colorupdate)

    #Final page setup
    page.add(
            ft.Text("Red value"),
            redslider,
            ft.Text("Green value"),
            greenslider,
            ft.Text("Blue value"),
            blueslider,
            rgb_text
        )
ft.run(main=main)


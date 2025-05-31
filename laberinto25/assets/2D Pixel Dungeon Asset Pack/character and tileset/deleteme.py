import pygame

def load_sprite_sheet(filename, sprite_width, sprite_height):
    sprite_sheet = pygame.image.load(filename).convert_alpha()
    sheet_width, sheet_height = sprite_sheet.get_size()
    sprites = []
    
    for y in range(0, sheet_height, sprite_height):
        for x in range(0, sheet_width, sprite_width):
            rect = pygame.Rect(x, y, sprite_width, sprite_height)
            sprite = sprite_sheet.subsurface(rect)
            sprites.append(sprite)
    
    return sprites

# Example usage
pygame.init()
screen = pygame.display.set_mode((1200, 1200))

# Load the sprite sheet
filename = 'assets/2D Pixel Dungeon Asset Pack/character and tileset/Dungeon_Character.png'  # Replace with your sprite sheet file

# Test different dimensions
test_dimensions = [(16, 16)]
sprites = []

for width, height in test_dimensions:
    sprites = load_sprite_sheet(filename, width, height)
    if sprites:  # If sprites were loaded
        break  # Exit the loop if successful

# Scale up the sprite
scaled_sprites = [pygame.transform.scale(sprite, (64, 64)) for sprite in sprites]

# Main loop to display the first sprite
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))  # Clear the screen with white
    if scaled_sprites:
        offset = 0
        yset = 0
        for sprite in scaled_sprites:
            offset += 69
            if offset >= 1200:
                offset = 0
                yset += 69
            screen.blit(sprite, (offset, yset))
    pygame.display.flip()  # Update the display

pygame.quit()

import pygame
import sys

# Inicializar pygame
pygame.init()
width, height = 1000, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Máquina de Turing - Interfaz")

# Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GRAY = (200, 200, 200)

# Variables
alphabet = ""
input_string = ""
head_pos = 0
font = pygame.font.Font(None, 28)
movements = []

# Rectángulos para las áreas de los groupboxes
groupbox_entry_rect = pygame.Rect(20, 20, 200, 100)
groupbox_chain_rect = pygame.Rect(240, 20, 700, 100)
groupbox_actions_rect = pygame.Rect(20, 140, 200, 440)
groupbox_movements_rect = pygame.Rect(240, 140, 700, 440)

# Función para dibujar un GroupBox
def draw_groupbox(rect, title, content=None):
    pygame.draw.rect(screen, BLACK, rect, 2)
    title_surf = font.render(title, True, BLACK)
    screen.blit(title_surf, (rect.x + 10, rect.y - 30))

# Función para manejar la visualización de la cadena con el cabezal
def draw_chain(head_position, chain_string, rect):
    pygame.draw.rect(screen, GRAY, rect)
    pygame.draw.rect(screen, BLACK, rect, 2)

    chain_font = pygame.font.Font(None, 36)
    head_font = pygame.font.Font(None, 28)

    # Dibuja la cadena
    if chain_string:
        chain_surf = chain_font.render(chain_string, True, BLACK)
        screen.blit(chain_surf, (rect.x + 10, rect.y + 30))

    # Dibuja el cabezal (flecha que apunta al caracter actual)
    head_indicator = "▼"
    head_surf = head_font.render(head_indicator, True, BLUE)
    head_x = rect.x + 10 + head_position * 28  # Ajuste de la posición del cabezal
    screen.blit(head_surf, (head_x, rect.y + 5))

# Función para dibujar el cuadro de movimientos
def draw_movements(rect, movement_list):
    pygame.draw.rect(screen, GRAY, rect)
    pygame.draw.rect(screen, BLACK, rect, 2)

    movement_font = pygame.font.Font(None, 28)
    for i, move in enumerate(movement_list[-12:]):  # Solo mostramos los últimos 12 movimientos
        move_surf = movement_font.render(move, True, BLACK)
        screen.blit(move_surf, (rect.x + 10, rect.y + 10 + i * 30))

# Función principal
def main():
    global alphabet, input_string, head_pos

    # Elementos de la interfaz
    alphabet_label = font.render("Alfabeto:", True, BLACK)
    input_string_label = font.render("Cadena:", True, BLACK)

    alphabet_textbox = pygame.Rect(30, 60, 160, 30)
    input_string_textbox = pygame.Rect(30, 100, 160, 30)

    # Botones de acciones y listboxes
    buscar_button = pygame.Rect(30, 160, 160, 30)
    buscar_second_button = pygame.Rect(30, 200, 160, 30)
    listbox_buscar = pygame.Rect(30, 240, 160, 60)

    mover_izquierda_button = pygame.Rect(30, 320, 160, 30)
    mover_derecha_button = pygame.Rect(30, 360, 160, 30)

    sobreescribir_button = pygame.Rect(30, 400, 160, 30)
    listbox_sobreescribir = pygame.Rect(30, 440, 160, 60)

    marcar_button = pygame.Rect(30, 510, 160, 30)
    listbox_marcar = pygame.Rect(30, 550, 160, 40)

    guardar_button = pygame.Rect(240, 600, 160, 30)

    # Bucle principal
    clock = pygame.time.Clock()
    while True:
        screen.fill(WHITE)

        # Dibujar GroupBoxes y etiquetas de "Entrada"
        draw_groupbox(groupbox_entry_rect, "Entrada")
        screen.blit(alphabet_label, (groupbox_entry_rect.x + 10, groupbox_entry_rect.y + 10))
        screen.blit(input_string_label, (groupbox_entry_rect.x + 10, groupbox_entry_rect.y + 50))

        pygame.draw.rect(screen, WHITE, alphabet_textbox)
        pygame.draw.rect(screen, BLACK, alphabet_textbox, 2)

        pygame.draw.rect(screen, WHITE, input_string_textbox)
        pygame.draw.rect(screen, BLACK, input_string_textbox, 2)

        # Dibujar GroupBox de "Cadena"
        draw_groupbox(groupbox_chain_rect, "Cadena")
        draw_chain(head_pos, input_string, groupbox_chain_rect)

        # Dibujar GroupBox de "Acciones"
        draw_groupbox(groupbox_actions_rect, "Acciones")

        # Botones y listboxes
        pygame.draw.rect(screen, GRAY, buscar_button)
        screen.blit(font.render("Buscar", True, BLACK), (buscar_button.x + 40, buscar_button.y + 5))

        pygame.draw.rect(screen, GRAY, buscar_second_button)
        screen.blit(font.render("Buscar Segundo", True, BLACK), (buscar_second_button.x + 10, buscar_second_button.y + 5))

        pygame.draw.rect(screen, GRAY, mover_izquierda_button)
        screen.blit(font.render("Mover Izquierda", True, BLACK), (mover_izquierda_button.x + 10, mover_izquierda_button.y + 5))

        pygame.draw.rect(screen, GRAY, mover_derecha_button)
        screen.blit(font.render("Mover Derecha", True, BLACK), (mover_derecha_button.x + 10, mover_derecha_button.y + 5))

        pygame.draw.rect(screen, GRAY, sobreescribir_button)
        screen.blit(font.render("Sobreescribir", True, BLACK), (sobreescribir_button.x + 20, sobreescribir_button.y + 5))

        pygame.draw.rect(screen, GRAY, marcar_button)
        screen.blit(font.render("Marcar", True, BLACK), (marcar_button.x + 40, marcar_button.y + 5))

        pygame.draw.rect(screen, GRAY, guardar_button)
        screen.blit(font.render("Guardar", True, BLACK), (guardar_button.x + 40, guardar_button.y + 5))

        # Dibujar el ListBox y cuadro de movimientos
        draw_movements(groupbox_movements_rect, movements)

        # Eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.flip()
        clock.tick(30)

if __name__ == "__main__":
    main()

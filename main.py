import pygame
import math

pygame.init()
pygame.font.init()
font = pygame.font.Font(pygame.font.get_default_font(), 18)

WIDTH = 800
HEIGHT = 600
canvas = pygame.display.set_mode((WIDTH, HEIGHT))
positions = []
edges = []

class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        

    
def visualize_binary_tree(root):
    idx = 0
    rect_color = (255, 0, 0)
    edge_color = (0, 0, 0)

    def calculate_positions(node, x, y, x_off, y_step):
        if node:
            positions.append((node, (x,y)))
            if node.left:
                edges.append(((x,y), (x-x_off, y + 2 * y_step)))
                calculate_positions(node.left, x-x_off, y + 2 * y_step, x_off // 2, y_step)
            if node.right:
                edges.append(((x,y), (x+x_off, y + 2 * y_step)))
                calculate_positions(node.right, x+x_off, y + 2*  y_step, x_off // 2, y_step)
    

        
    pygame.display.set_caption("Binary Tree Visualizer")
    exit = False
    while not exit:
        canvas.fill((255, 255, 255)) 
        for event in pygame.event.get():
            if(event.type == pygame.QUIT):
                exit= True
            if(event.type == pygame.KEYDOWN):
                if event.key == pygame.K_i:
                    user_input = input("Enter a value to insert: ").strip()
                    if user_input.isdigit():  
                        if int(user_input) > 999:
                            print("Value too large. Operation canceled.")
                            user_input = ""
                            break
                        else:
                            root = insert(root, int(user_input))
                            calculate_positions(root, WIDTH // 2, 50, WIDTH // 4, 75)

                    else:
                        print("Invalid input. Please enter a numeric value.")
                        user_input = ""  
                if event.key == pygame.K_d:
                    print("Delete operation selected.")

        for start, end in edges:
            pygame.draw.line(canvas, edge_color, start, end, 2)

        # Draw nodes
        for node, (x, y) in positions:
            pygame.draw.circle(canvas, rect_color, (x, y), 20)
            text_surface = font.render(str(node.key), True, (0,0,0))
            canvas.blit(text_surface, dest=(x-5,y-5))

        pygame.display.update()

    
    
def insert(root, key):
    if root is None:
        return TreeNode(key)
    else:
        if key < root.key:
            root.left = insert(root.left, key)
        else:
            root.right = insert(root.right, key)
    return root

def delete(root, key):
    
    if root is None:
        return root
    
    if key < root.key:
        root.left = delete(root.left, key)
    elif key > root.key:
        root.right = delete(root.right, key)
    else:
        if root.left is None:
            temp = root.right
            root = None
            return temp
        elif root.right is None:
            temp = root.left
            root = None
            return temp
        
        temp = get_min_value(root.right)
        root.key = temp.key
        root.right = delete(root.right, temp.key)
    return root


def get_min_value(root):
    while root.left is not None:
        root = root.left
    return root

root = None
keys = []
for key in keys:
    root = insert(root, key)
    

visualize_binary_tree(root)

    

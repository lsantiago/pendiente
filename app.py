import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

def calculate_slope(x1, y1, x2, y2):
    """
    Calcula la pendiente entre dos puntos.
    
    Args:
        x1, y1: Coordenadas del primer punto
        x2, y2: Coordenadas del segundo punto
    
    Returns:
        float: La pendiente de la recta
    """
    if x2 - x1 == 0:
        return float('inf')  # Pendiente infinita (línea vertical)
    return (y2 - y1) / (x2 - x1)

def plot_line(x1, y1, x2, y2, slope):
    """
    Crea un gráfico de la línea que pasa por los dos puntos.
    
    Args:
        x1, y1: Coordenadas del primer punto
        x2, y2: Coordenadas del segundo punto
        slope: Pendiente de la recta
    """
    fig, ax = plt.subplots(figsize=(10, 8))
    
    # Puntos
    ax.plot([x1, x2], [y1, y2], 'bo-', markersize=8, linewidth=2, label='Línea')
    ax.plot(x1, y1, 'ro', markersize=10, label=f'Punto 1 ({x1}, {y1})')
    ax.plot(x2, y2, 'go', markersize=10, label=f'Punto 2 ({x2}, {y2})')
    
    # Extender la línea más allá de los puntos
    x_min = min(x1, x2) - 2
    x_max = max(x1, x2) + 2
    
    if slope != float('inf'):
        # Ecuación de la recta: y - y1 = m(x - x1)
        x_extended = np.linspace(x_min, x_max, 100)
        y_extended = y1 + slope * (x_extended - x1)
        ax.plot(x_extended, y_extended, 'b--', alpha=0.5, label='Extensión de la línea')
    else:
        # Línea vertical
        y_min = min(y1, y2) - 2
        y_max = max(y1, y2) + 2
        ax.axvline(x=x1, color='blue', linestyle='--', alpha=0.5, label='Línea vertical')
        ax.set_ylim(y_min, y_max)
    
    # Configuración del gráfico
    ax.grid(True, alpha=0.3)
    ax.set_xlabel('X', fontsize=12)
    ax.set_ylabel('Y', fontsize=12)
    ax.set_title(f'Línea entre dos puntos (Pendiente = {slope})', fontsize=14)
    ax.legend()
    ax.set_aspect('equal', adjustable='box')
    
    return fig

def main():
    st.title("📊 Calculadora de Pendiente")
    st.write("Ingresa las coordenadas de dos puntos para calcular la pendiente de la recta que los une.")
    
    # Crear dos columnas para organizar los inputs
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Punto 1")
        x1 = st.number_input("Coordenada X1:", value=0.0, step=0.1)
        y1 = st.number_input("Coordenada Y1:", value=0.0, step=0.1)
    
    with col2:
        st.subheader("Punto 2")
        x2 = st.number_input("Coordenada X2:", value=1.0, step=0.1)
        y2 = st.number_input("Coordenada Y2:", value=1.0, step=0.1)
    
    # Verificar que los puntos no sean idénticos
    if x1 == x2 and y1 == y2:
        st.error("⚠️ Los puntos no pueden ser idénticos. Por favor, ingresa coordenadas diferentes.")
        return
    
    # Calcular la pendiente
    slope = calculate_slope(x1, y1, x2, y2)
    
    # Mostrar resultados
    st.subheader("Resultados")
    
    if slope == float('inf'):
        st.success("🔢 **Pendiente:** Infinita (línea vertical)")
        st.info("La línea es vertical porque ambos puntos tienen la misma coordenada X.")
    else:
        st.success(f"🔢 **Pendiente:** {slope:.4f}")
        
        # Información adicional sobre la pendiente
        if slope > 0:
            st.info("📈 La línea tiene pendiente positiva (creciente)")
        elif slope < 0:
            st.info("📉 La línea tiene pendiente negativa (decreciente)")
        else:
            st.info("➡️ La línea es horizontal (pendiente cero)")
    
    # Mostrar la fórmula utilizada
    st.subheader("Fórmula")
    st.latex(r"m = \frac{y_2 - y_1}{x_2 - x_1}")
    
    if slope != float('inf'):
        st.write(f"m = ({y2} - {y1}) / ({x2} - {x1}) = {y2 - y1} / {x2 - x1} = {slope:.4f}")
    else:
        st.write(f"m = ({y2} - {y1}) / ({x2} - {x1}) = {y2 - y1} / 0 = ∞")
    
    # Opción para mostrar el gráfico
    st.subheader("Visualización")
    show_plot = st.checkbox("Mostrar gráfico", value=True)
    
    if show_plot:
        fig = plot_line(x1, y1, x2, y2, slope)
        st.pyplot(fig)
        
        # Información adicional sobre la ecuación de la recta
        st.subheader("Ecuación de la recta")
        if slope != float('inf'):
            b = y1 - slope * x1  # Intercepto en y
            st.write(f"**Forma pendiente-intercepto:** y = {slope:.4f}x + {b:.4f}")
            st.write(f"**Forma punto-pendiente:** y - {y1} = {slope:.4f}(x - {x1})")
        else:
            st.write(f"**Ecuación:** x = {x1}")

if __name__ == "__main__":
    main()
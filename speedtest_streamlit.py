# speedtest_streamlit.py
import streamlit as st
import speedtest

def testar_velocidade():
    st.title("🌐 Testador de Velocidade de Internet")
    
    if st.button("Iniciar Teste"):
        try:
            with st.spinner("Testando..."):
                s = speedtest.Speedtest()
                s.get_best_server()
                
                download = s.download() / 1_000_00  # Mbps
                upload = s.upload() / 1_000_00
                ping = s.results.ping
                
                st.metric("Download", f"{download:.2f} Mbps")
                st.metric("Upload", f"{upload:.2f} Mbps")
                st.metric("Ping", f"{ping:.2f} ms")
                
        except Exception as e:
            st.error("Erro ao testar a velocidade!")

if __name__ == "__main__":
    testar_velocidade()

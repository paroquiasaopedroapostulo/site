@echo off
title Painel de Atualizacao - Paroquia Sao Pedro Apostolo
cls
echo =======================================================
echo    PAINEL DE ATUALIZACAO LITURGICA - 30 ANOS
echo =======================================================
echo.

set /p versiculo="Digite o Versiculo (sem aspas): "
set /p ref="Digite a Referencia (ex: Mateus 5:1): "
set /p reflexao="Digite a Reflexao do Padre: "

echo.
echo Atualizando o arquivo index.html...
echo.

python atualizar_site.py "%versiculo%" "%ref%" "%reflexao%"

echo.
echo =======================================================
echo Finalizado! Pressione qualquer tecla para sair.

echo Enviando atualizacao para o GitHub...
git add index.html
git commit -m "Atualizacao de versiculo semanal"
git push origin main
echo Site atualizado na internet com sucesso!
pause > nul
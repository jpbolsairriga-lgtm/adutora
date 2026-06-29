// ── Bolsa Irriga — Email Sender ──────────────────────────────────────
// Cole este código em script.google.com → Novo projeto
// Depois: Implantar → Nova implantação → App da web
//   Executar como: Eu mesmo
//   Quem tem acesso: Qualquer pessoa
// Copie a URL gerada e cole no campo "URL do Script" dentro da app.
// ─────────────────────────────────────────────────────────────────────

const DESTINATARIO = 'jp.bolsairriga@yahoo.com.br';

function doPost(e) {
  try {
    const data = JSON.parse(e.postData.contents);

    const pdfBytes = Utilities.base64Decode(data.pdf_base64);
    const pdfBlob  = Utilities.newBlob(pdfBytes, 'application/pdf', data.filename || 'relatorio.pdf');

    GmailApp.sendEmail(
      DESTINATARIO,
      data.subject,
      data.body,
      { attachments: [pdfBlob], name: 'Bolsa Irriga — Relatório' }
    );

    return resposta({ status: 'ok', mensagem: 'E-mail enviado com sucesso.' });

  } catch (err) {
    return resposta({ status: 'erro', mensagem: err.message });
  }
}

function resposta(obj) {
  return ContentService
    .createTextOutput(JSON.stringify(obj))
    .setMimeType(ContentService.MimeType.JSON);
}

// Permite testar manualmente no editor do Apps Script
function testar() {
  GmailApp.sendEmail(DESTINATARIO, 'Teste Bolsa Irriga', 'Teste de envio OK.');
  Logger.log('E-mail de teste enviado para ' + DESTINATARIO);
}

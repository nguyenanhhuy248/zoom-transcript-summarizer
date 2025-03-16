import { useState } from 'react';
import { 
  Box, 
  Container, 
  TextField, 
  Typography, 
  Paper,
  Button,
  Fade,
} from '@mui/material';
import { FileUploader } from '../../components/FileUploader/FileUploader';
import { uploadTranscript } from '../../services/api';

export const Home = () => {
  const [file, setFile] = useState<File | null>(null);
  const [summary, setSummary] = useState('');
  const [loading, setLoading] = useState(false);

  const handleUpload = async () => {
    if (!file) return;

    setSummary('');
    setLoading(true);
    try {
      const response = await uploadTranscript(file);
      setSummary(response.summary);
    } catch (error) {
      console.error('Error uploading file:', error);
      alert('Error uploading file. Please try again.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <Box
      sx={{
        minHeight: '100vh',
        display: 'flex',
        flexDirection: 'column',
        alignItems: 'center',
        justifyContent: 'center',
        background: 'linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%)',
        p: 4,
      }}
    >
      <Container 
        maxWidth="md"
        sx={{
          display: 'flex',
          flexDirection: 'column',
          alignItems: 'center',
        }}
      >
        <Fade in timeout={1000}>
          <Box sx={{ textAlign: 'center', mb: 4, maxWidth: '800px', width: '100%' }}>
            <Typography
              variant="h3"
              component="h1"
              gutterBottom
              noWrap
              sx={{
                fontWeight: 700,
                background: 'linear-gradient(45deg, #2196f3 30%, #21CBF3 90%)',
                backgroundClip: 'text',
                textFillColor: 'transparent',
                WebkitBackgroundClip: 'text',
                WebkitTextFillColor: 'transparent',
                mb: 2,
                fontSize: { xs: '1.8rem', sm: '2.4rem', md: '3rem' },
                whiteSpace: 'nowrap',
              }}
            >
              Zoom Transcript Summarizer
            </Typography>
            <Typography variant="h6" color="text.secondary" sx={{ mb: 4 }}>
              Upload your transcript and get an AI-powered summary
            </Typography>
          </Box>
        </Fade>

        <Fade in timeout={1500}>
          <Paper 
            elevation={3} 
            sx={{ 
              p: 4,
              borderRadius: 3,
              background: 'rgba(255, 255, 255, 0.9)',
              backdropFilter: 'blur(10px)',
              transition: 'transform 0.3s ease-in-out, box-shadow 0.3s ease-in-out',
              '&:hover': {
                transform: 'translateY(-5px)',
                boxShadow: '0 12px 40px rgba(0,0,0,0.12)',
              },
              width: '100%',
              maxWidth: '800px',
              mx: 'auto',
            }}
          >
            <FileUploader
              file={file}
              onFileChange={setFile}
              onUpload={handleUpload}
              loading={loading}
            />

            <TextField
              fullWidth
              multiline
              rows={10}
              variant="outlined"
              value={summary}
              onChange={(e) => setSummary(e.target.value)}
              placeholder="Your summary will appear here..."
              sx={{
                mb: 3,
                '& .MuiOutlinedInput-root': {
                  backgroundColor: 'background.paper',
                  '&:hover': {
                    '& > fieldset': {
                      borderColor: 'primary.main',
                    },
                  },
                },
              }}
            />

            <Box sx={{ display: 'flex', justifyContent: 'center' }}>
              <Button
                variant="outlined"
                onClick={() => navigator.clipboard.writeText(summary)}
                disabled={!summary}
                sx={{
                  borderWidth: 2,
                  '&:hover': {
                    borderWidth: 2,
                  },
                }}
                startIcon={<span>📋</span>}
              >
                Copy to Clipboard
              </Button>
            </Box>
          </Paper>
        </Fade>
      </Container>
    </Box>
  );
}; 
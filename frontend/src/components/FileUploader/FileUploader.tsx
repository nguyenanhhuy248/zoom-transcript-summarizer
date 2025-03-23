import { useRef } from "react";
import { Box, Button, Typography, IconButton } from "@mui/material";

interface FileUploaderProps {
  file: File | null;
  onFileChange: (file: File | null) => void;
  onUpload: () => void;
  loading: boolean;
}

export const FileUploader = ({
  file,
  onFileChange,
  onUpload,
  loading,
}: FileUploaderProps) => {
  const fileInputRef = useRef<HTMLInputElement>(null);

  const handleFileChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    if (event.target.files && event.target.files[0]) {
      onFileChange(event.target.files[0]);
    }
  };

  const handleRemoveFile = () => {
    onFileChange(null);
    if (fileInputRef.current) {
      fileInputRef.current.value = "";
    }
  };

  return (
    <Box
      sx={{
        width: "100%",
        display: "flex",
        flexDirection: "column",
        alignItems: "center",
      }}
    >
      <Box
        sx={{
          display: "flex",
          gap: 2,
          mb: 4,
          width: "100%",
          flexDirection: { xs: "column", sm: "row" },
          justifyContent: "center",
        }}
      >
        <Button
          variant="contained"
          component="label"
          fullWidth
          sx={{
            height: 56,
            maxWidth: { xs: "100%", sm: "250px" },
            background: "linear-gradient(45deg, #2196f3 30%, #21CBF3 90%)",
            "&:hover": {
              background: "linear-gradient(45deg, #1976d2 30%, #1ba9d2 90%)",
            },
          }}
        >
          Choose File
          <input
            type="file"
            hidden
            ref={fileInputRef}
            onChange={handleFileChange}
            accept=".vtt,.txt"
          />
        </Button>
        <Button
          variant="contained"
          color="secondary"
          onClick={onUpload}
          disabled={!file || loading}
          fullWidth
          sx={{
            height: 56,
            maxWidth: { xs: "100%", sm: "250px" },
            background: loading
              ? undefined
              : "linear-gradient(45deg, #0288d1 30%, #03a9f4 90%)",
            "&:hover": {
              background: loading
                ? undefined
                : "linear-gradient(45deg, #01579b 30%, #0288d1 90%)",
            },
            color: "white",
          }}
        >
          {loading ? "Processing..." : "Upload & Summarize"}
        </Button>
      </Box>

      {file && (
        <Box
          sx={{
            mb: 3,
            p: 2,
            borderRadius: 2,
            backgroundColor: "rgba(33, 150, 243, 0.1)",
            color: "primary.main",
            display: "flex",
            alignItems: "center",
            justifyContent: "space-between",
            width: "100%",
            maxWidth: "600px",
          }}
        >
          <Typography
            variant="body2"
            sx={{
              display: "flex",
              alignItems: "center",
              gap: 1,
            }}
          >
            📄 Selected file: {file.name}
          </Typography>
          <IconButton
            onClick={handleRemoveFile}
            size="small"
            sx={{
              color: "primary.main",
              "&:hover": {
                backgroundColor: "rgba(33, 150, 243, 0.2)",
              },
            }}
          >
            <span style={{ fontSize: "1.2rem" }}>✕</span>
          </IconButton>
        </Box>
      )}
    </Box>
  );
};

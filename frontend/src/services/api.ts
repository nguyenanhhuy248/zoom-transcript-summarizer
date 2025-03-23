import axios from "axios";

const API_BASE_URL = "http://localhost:8000";

export const uploadTranscript = async (
  file: File,
): Promise<{ summary: string }> => {
  const formData = new FormData();
  formData.append("file", file);

  const response = await axios.post(
    `${API_BASE_URL}/api/v1/summarize`,
    formData,
  );
  return response.data;
};

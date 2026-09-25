import { LandingPage } from './landing/LandingPage';

export default function App() {
  const handleStartApp = () => {
    alert("Don't Stop o'yiniga xush kelibsiz! APK / Web Versiya tez orada taqdim etiladi.");
  };

  const handleOpenLeaderboard = () => {
    alert("Gildiyalar va O'yinchilar reytingi real-vaqt rejimida yangilanib turadi.");
  };

  return (
    <div style={{ minHeight: '100vh', backgroundColor: '#0b0f19' }}>
      <LandingPage onStartApp={handleStartApp} onOpenLeaderboard={handleOpenLeaderboard} />
    </div>
  );
}

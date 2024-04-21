namespace App\Models;
use Illuminate\Database\Eloquent\Model;

class User extends Model {
    protected $fillable = ['name', 'email', 'password', 'unique_id'];
}

// app/Models/VitalSign.php
namespace App\Models;
use Illuminate\Database\Eloquent\Model;

class VitalSign extends Model {
    protected $fillable = ['user_id', 'pulse_rate', 'oxygen_level', 'temperature', 'accelerometer_data', 'gyroscope_data'];
}

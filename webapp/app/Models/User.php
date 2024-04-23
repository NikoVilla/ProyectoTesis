<?php

namespace App\Models;

// use Illuminate\Contracts\Auth\MustVerifyEmail;
use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Foundation\Auth\User as Authenticatable;
use Illuminate\Notifications\Notifiable;

class User extends Authenticatable
{
    use HasFactory, Notifiable;

    /**
     * The attributes that are mass assignable.
     *
     * @var array<int, string>
     */
    protected $fillable = [
        'name',
        'email',
        'password',
    ];

    /**
     * The attributes that should be hidden for serialization.
     *
     * @var array<int, string>
     */
    protected $hidden = [
        'password',
        'remember_token',
    ];

    /**
     * Get the attributes that should be cast.
     *
     * @return array<string, string>
     */
    protected function casts(): array
    {
        return [
            'email_verified_at' => 'datetime',
            'password' => 'hashed',
        ];
    }
}

// namespace App\Models;
//use Illuminate\Database\Eloquent\Model;

//class User extends Model {
//    protected $fillable = ['name', 'email', 'password', 'unique_id'];
//}

// app/Models/VitalSign.php
//namespace App\Models;
//use Illuminate\Database\Eloquent\Model;

//class VitalSign extends Model {
//    protected $fillable = ['user_id', 'pulse_rate', 'oxygen_level', 'temperature', 'accelerometer_data', 'gyroscope_data'];
//}
